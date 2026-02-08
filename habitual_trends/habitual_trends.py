import reflex as rx
import httpx
from typing import List, Dict

# CONFIG: Points to your live Render backend
BACKEND_URL = "https://habitual-trends.onrender.com/api/habits"

# --- 1. STATE & LOGIC ---
class State(rx.State):
    """The app state managing data and communication."""
    habits: List[Dict] = []
    new_habit_name: str = ""
    
    # Auth State
    logged_in: bool = False
    user_email: str = ""

    # Dashboard Computed Stats
    @rx.var
    def total_habits(self) -> int:
        return len(self.habits)

    @rx.var
    def top_streak(self) -> int:
        streaks = [h["streak"] for h in self.habits]
        return max(streaks) if streaks else 0

    def login(self):
        """Simulate login and fetch initial data."""
        if self.user_email:
            self.logged_in = True
            return State.fetch_habits

    def logout(self):
        """Reset the app state."""
        self.logged_in = False
        self.user_email = ""
        self.habits = []

    async def fetch_habits(self):
        """Fetch habits from the live FastAPI backend."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(BACKEND_URL)
                if response.status_code == 200:
                    self.habits = response.json()
            except Exception as e:
                print(f"Error fetching: {e}")

    async def add_habit(self):
        """POST a new habit to the backend."""
        if not self.new_habit_name.strip():
            return
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    BACKEND_URL, 
                    json={"name": self.new_habit_name}
                )
                if response.status_code in [200, 201]:
                    self.new_habit_name = ""
                    yield State.fetch_habits
            except Exception as e:
                print(f"Error adding: {e}")

    async def increment_streak(self, habit_id: int):
        """PUT request to increment habit streak."""
        async with httpx.AsyncClient() as client:
            try:
                # Matches backend: /api/habits/{id}/increment
                response = await client.put(f"{BACKEND_URL}/{habit_id}/increment")
                if response.status_code == 200:
                    yield State.fetch_habits
            except Exception as e:
                print(f"Error incrementing: {e}")

    async def delete_habit(self, habit_id: int):
        """DELETE a habit and refresh."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(f"{BACKEND_URL}/{habit_id}")
                if response.status_code == 200:
                    yield State.fetch_habits  
            except Exception as e:
                print(f"Error deleting: {e}")

# --- 2. UI COMPONENTS ---

def stats_card(title: str, value: any, subtext: str):
    return rx.vstack(
        rx.text(title, color="#a0aec0", font_size="0.9em", font_weight="bold"),
        rx.text(value, color="cyan", font_size="2.2em", font_weight="bold"),
        rx.text(subtext, color="white", font_size="0.8em"),
        bg="rgba(18, 25, 45, 0.8)",
        backdrop_filter="blur(10px)",
        padding="1.5em",
        border_radius="15px",
        border="1px solid rgba(255, 255, 255, 0.1)",
        width="100%",
        align_items="start",
    )

def habit_item(habit: Dict):
    return rx.hstack(
        rx.hstack(
            rx.icon_button(
                rx.icon(tag="check", size=18),
                on_click=lambda: State.increment_streak(habit["id"]),
                color_scheme="green",
                variant="soft",
                cursor="pointer",
            ),
            rx.text(habit["name"], color="white", font_weight="medium"),
            spacing="3",
        ),
        rx.hstack(
            rx.badge(f"🔥 {habit['streak']}", color_scheme="cyan", variant="outline", font_size="0.9em"),
            rx.icon_button(
                rx.icon(tag="trash_2", size=16),
                on_click=lambda: State.delete_habit(habit["id"]),
                variant="ghost",
                color_scheme="red",
                cursor="pointer",
            ),
            spacing="4",
            align="center",
        ),
        justify="between", 
        width="100%",
        padding="1em",
        border_bottom="1px solid rgba(255, 255, 255, 0.05)",
    )

def login_page():
    return rx.center(
        rx.vstack(
            rx.icon(tag="activity", color="cyan", size=50),
            rx.heading("HABITUAL TRENDS", size="8", color="cyan", letter_spacing="2px"),
            rx.text("Track your progress in real-time.", color="gray", margin_bottom="1em"),
            rx.input(
                placeholder="Enter Email", 
                on_change=State.set_user_email,
                width="100%",
                bg="rgba(255,255,255,0.05)",
                color="white"
            ),
            rx.button(
                "Launch Dashboard", 
                on_click=State.login, 
                width="100%", 
                color_scheme="cyan",
                cursor="pointer"
            ),
            padding="3em",
            bg="#0B1120",
            border_radius="20px",
            border="1px solid #1f2937",
            spacing="4",
            box_shadow="0 10px 30px rgba(0,0,0,0.5)"
        ),
        height="100vh",
        bg="#070b14"
    )

def dashboard_view():
    return rx.hstack(
        # Sidebar
        rx.vstack(
            rx.vstack(
                rx.icon(tag="activity", color="cyan", size=30),
                rx.heading("HABITUAL", size="4", color="cyan"),
                align_items="center",
                padding_bottom="2em",
            ),
            rx.text(f"User: {State.user_email}", size="1", color="gray"),
            rx.spacer(),
            rx.button("Logout", on_click=State.logout, variant="ghost", color_scheme="red", width="100%"),
            bg="#0B1120",
            height="100vh",
            width="240px",
            padding="2em",
            border_right="1px solid #1f2937",
        ),
        # Main Content
        rx.vstack(
            rx.heading("Dashboard Overview", color="white", size="7", margin_bottom="1em"),
            rx.grid(
                stats_card("Active Habits", State.total_habits, "Tracking"),
                stats_card("Top Streak", State.top_streak, "Current Best"),
                stats_card("Completion", "85%", "Daily Average"),
                columns="3",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.heading("My Habits", size="5", color="white", margin_top="2em"),
                rx.hstack(
                    rx.input(
                        placeholder="Add a new habit...", 
                        on_change=State.set_new_habit_name,
                        value=State.new_habit_name,
                        bg="rgba(255, 255, 255, 0.05)",
                        color="white",
                        width="300px"
                    ),
                    rx.button("Add", on_click=State.add_habit, bg="cyan", color="black"),
                    spacing="4",
                ),
                rx.vstack(
                    rx.foreach(State.habits, habit_item),
                    width="100%",
                    bg="rgba(18, 25, 45, 0.5)",
                    border_radius="12px",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    margin_top="1em"
                ),
                align_items="start",
                width="100%",
            ),
            bg="#0f172a",
            width="100%",
            height="100vh",
            padding="3em",
            overflow_y="auto",
        ),
        spacing="0",
    )

# --- 3. MAIN PAGE ROUTING ---
def index():
    return rx.cond(
        State.logged_in,
        dashboard_view(),
        login_page()
    )

app = rx.App(
    style={
        "background_color": "#070b14",
        "font_family": "Inter, sans-serif",
    }
)
app.add_page(index)