import reflex as rx
import httpx
from typing import List, Dict

# CONFIG: URL for your Python FastAPI backend
BACKEND_URL = "http://127.0.0.1:3005/api/habits"

class State(rx.State):
    """The app state managing data, security, and dynamic calculations."""
    habits: List[Dict] = []
    new_habit_name: str = ""
    
    # Login State
    logged_in: bool = False
    password_input: str = ""
    
    # Dashboard Stats
    total_habits: int = 0
    streak: int = 12 # Global streak mock

    @rx.var
    def completion_rate(self) -> str:
        """Calculates percentage of habits with at least 1 streak point."""
        if not self.habits:
            return "0%"
        completed = len([h for h in self.habits if h["streak"] > 0])
        rate = (completed / len(self.habits)) * 100
        return f"{int(rate)}%"

    async def fetch_habits(self):
        """Fetch habits from the FastAPI backend."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(BACKEND_URL)
                if response.status_code == 200:
                    self.habits = response.json()
                    self.total_habits = len(self.habits)
            except Exception as e:
                print(f"Error fetching: {e}")

    async def add_habit(self):
        """Send new habit to backend and refresh."""
        if not self.new_habit_name.strip():
            return
        async with httpx.AsyncClient() as client:
            try:
                await client.post(BACKEND_URL, json={"name": self.new_habit_name})
                self.new_habit_name = ""
                yield State.fetch_habits
            except Exception as e:
                print(f"Error adding: {e}")

    async def increment_streak(self, habit_id: int):
        """Logic for the green checkmark button."""
        async with httpx.AsyncClient() as client:
            try:
                await client.put(f"{BACKEND_URL}/{habit_id}/increment")
                yield State.fetch_habits
            except Exception as e:
                print(f"Error incrementing: {e}")

    async def delete_habit(self, habit_id: int):
        """Logic for the trash button."""
        async with httpx.AsyncClient() as client:
            try:
                await client.delete(f"{BACKEND_URL}/{habit_id}")
                yield State.fetch_habits
            except Exception as e:
                print(f"Error deleting: {e}")

    def login(self):
        """Simple password check."""
        if self.password_input == "habit123":
            self.logged_in = True
            return State.fetch_habits
        else:
            return rx.window_alert("Incorrect Password")

    def logout(self):
        self.logged_in = False
        self.password_input = ""

    def on_load(self):
        if self.logged_in:
            return State.fetch_habits

# --- UI COMPONENTS ---

def habit_item(habit: Dict):
    """Component for a single habit row."""
    return rx.hstack(
        rx.hstack(
            rx.icon(tag="circle", size=18, color="gray"),
            rx.text(habit["name"], color="white", font_weight="medium"),
            spacing="3",
        ),
        rx.hstack(
            rx.button(
                rx.icon(tag="check", size=16),
                on_click=lambda: State.increment_streak(habit["id"]),
                color_scheme="green", variant="soft", size="1",
                cursor="pointer",
            ),
            rx.badge(f"Streak: {habit['streak']}", color_scheme="cyan", variant="outline"),
            rx.icon_button(
                rx.icon(tag="trash_2", size=16),
                on_click=lambda: State.delete_habit(habit["id"]),
                variant="ghost", color_scheme="red", size="1",
                cursor="pointer",
            ),
            spacing="3",
            align="center",
        ),
        justify="between", width="100%", padding="1em",
        border_bottom="1px solid rgba(255, 255, 255, 0.05)",
    )

def stats_card(title: str, value: rx.Var, subtext: str):
    """Reusable card for dashboard statistics."""
    return rx.vstack(
        rx.text(title, color="#a0aec0", font_size="0.9em", font_weight="bold"),
        rx.text(value, color="cyan", font_size="2em", font_weight="bold"),
        rx.text(subtext, color="white", font_size="0.8em"),
        bg="rgba(18, 25, 45, 0.8)", padding="1.5em", border_radius="15px",
        border="1px solid rgba(255, 255, 255, 0.1)", width="100%", align_items="start",
    )

# --- PAGE LAYOUT ---

def index():
    return rx.fragment(
        rx.cond(
            State.logged_in,
            # DASHBOARD VIEW
            rx.hstack(
                rx.vstack( # Sidebar
                    rx.vstack(
                        rx.icon(tag="activity", color="cyan", size=30),
                        rx.heading("HABITUAL", size="4", color="cyan"),
                        align_items="center", spacing="2", padding_bottom="2em"
                    ),
                    rx.button("Logout", on_click=State.logout, variant="ghost", color_scheme="red", size="2", width="100%"),
                    bg="#0B1120", height="100vh", width="250px", padding="2em", border_right="1px solid #1f2937",
                ),
                rx.vstack( # Main Content Area
                    rx.heading("Dashboard Overview", color="white", size="7", margin_bottom="1em"),
                    rx.grid(
                        stats_card("Global Streak", State.streak, "Days Active"),
                        stats_card("Completion", State.completion_rate, "Today's Target"),
                        stats_card("Active Habits", State.total_habits, "Tracking Now"),
                        columns="3", spacing="5", width="100%",
                    ),
                    rx.vstack( # Habit Management Section
                        rx.heading("Manage Habits", size="5", color="white", margin_top="2em"),
                        rx.hstack(
                            rx.input(
                                placeholder="New habit...", 
                                on_change=State.set_new_habit_name, 
                                value=State.new_habit_name, 
                                bg="rgba(255,255,255,0.05)", color="white", width="300px"
                            ),
                            rx.button("Create", on_click=State.add_habit, bg="cyan", color="black"),
                            spacing="3"
                        ),
                        rx.vstack(
                            rx.foreach(State.habits, habit_item),
                            width="100%", bg="rgba(18,25,45,0.5)", border_radius="12px", 
                            padding="1em", margin_top="1em"
                        ),
                        align_items="start", width="100%"
                    ),
                    bg="#0f172a", width="100%", height="100vh", padding="3em", overflow_y="auto",
                ),
                spacing="0",
            ),
            # LOGIN VIEW
            rx.center(
                rx.vstack(
                    rx.heading("Habitual Login", color="white", size="6"),
                    rx.text("Secure AI Habit Tracker", color="#a0aec0"),
                    rx.input(
                        placeholder="Enter Password", 
                        type="password", 
                        on_change=State.set_password_input, 
                        bg="rgba(255,255,255,0.1)", color="white", width="100%"
                    ),
                    rx.button("Enter Dashboard", on_click=State.login, bg="cyan", color="black", width="100%"),
                    spacing="4", padding="4em", bg="#0B1120", border_radius="20px", border="1px solid cyan"
                ),
                height="100vh", bg="#0B1120"
            )
        )
    )

app = rx.App()
app.add_page(index, on_load=State.on_load)