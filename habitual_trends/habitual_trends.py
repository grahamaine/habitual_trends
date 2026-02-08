import reflex as rx
import httpx
from typing import List, Dict

# CONFIG: URL for your Python FastAPI backend
BACKEND_URL = "http://127.0.0.1:3005/api/habits"

# --- 1. STATE & LOGIC ---
class State(rx.State):
    """The app state managing data and communication."""
    habits: List[Dict] = []
    new_habit_name: str = ""
    
    # Dashboard Mock Stats
    streak: int = 12
    completion: str = "85%"
    total_habits: int = 0

    async def fetch_habits(self):
        """Fetch real habits from the SQLite database via the FastAPI backend."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(BACKEND_URL)
                if response.status_code == 200:
                    self.habits = response.json()
                    self.total_habits = len(self.habits)
            except Exception as e:
                print(f"Error fetching habits: {e}")

    async def add_habit(self):
        """Send a new habit to the database and refresh the UI."""
        if not self.new_habit_name.strip():
            return
            
        async with httpx.AsyncClient() as client:
            try:
                await client.post(BACKEND_URL, json={"name": self.new_habit_name})
                self.new_habit_name = ""  
                await self.fetch_habits()  
            except Exception as e:
                print(f"Error adding habit: {e}")

    async def delete_habit(self, habit_id: int):
        """Delete a habit by ID and refresh the list."""
        async with httpx.AsyncClient() as client:
            try:
                # Calls the DELETE route on your FastAPI backend
                response = await client.delete(f"{BACKEND_URL}/{habit_id}")
                if response.status_code == 200:
                    await self.fetch_habits()  
            except Exception as e:
                print(f"Error deleting habit: {e}")

    def on_load(self):
        """Runs automatically when the page opens."""
        return State.fetch_habits

# --- 2. UI COMPONENTS ---

def stats_card(title: str, value: rx.Var, subtext: str):
    return rx.vstack(
        rx.text(title, color="#a0aec0", font_size="0.9em", font_weight="bold"),
        rx.text(value, color="cyan", font_size="2em", font_weight="bold"),
        rx.text(subtext, color="white", font_size="0.8em"),
        bg="rgba(18, 25, 45, 0.8)",
        backdrop_filter="blur(10px)",
        padding="1.5em",
        border_radius="15px",
        border="1px solid rgba(255, 255, 255, 0.1)",
        width="100%",
        align_items="start",
        box_shadow="0 4px 30px rgba(0, 0, 0, 0.5)",
    )

def sidebar():
    return rx.vstack(
        rx.vstack(
            rx.icon(tag="activity", color="cyan", size=40),
            rx.heading("HABITUAL", size="4", color="cyan", letter_spacing="2px"),
            rx.text("AI AGENT", size="1", color="white", letter_spacing="4px"),
            align_items="center",
            spacing="1",
            padding_bottom="3em",
        ),
        rx.vstack(
            rx.hstack(rx.icon(tag="layout_dashboard", color="cyan"), rx.text("Dashboard", color="white"), spacing="3"),
            rx.hstack(rx.icon(tag="list", color="cyan"), rx.text("My Habits", color="white"), spacing="3"),
            rx.hstack(rx.icon(tag="settings", color="cyan"), rx.text("Settings", color="white"), spacing="3"),
            align_items="start",
            spacing="6",
            width="100%"
        ),
        bg="#0B1120",
        height="100vh",
        width="280px",
        padding="2em",
        border_right="1px solid #1f2937",
        display=["none", "none", "flex", "flex"],
    )

def habit_item(habit: Dict):
    """A single row representing a habit in the list with a delete option."""
    return rx.hstack(
        rx.hstack(
            rx.icon(tag="circle", size=18, color="gray"),
            rx.text(habit["name"], color="white", font_weight="medium"),
            spacing="3",
        ),
        
        rx.hstack(
            rx.badge(f"Streak: {habit['streak']}", color_scheme="cyan", variant="outline"),
            
            # The new Delete Button
            rx.icon_button(
                rx.icon(tag="trash_2", size=16),
                on_click=lambda: State.delete_habit(habit["id"]),
                variant="ghost",
                color_scheme="red",
                cursor="pointer",
                _hover={"bg": "rgba(255, 0, 0, 0.1)"},
            ),
            spacing="4",
            align="center",
        ),
        
        justify="between", 
        width="100%",
        padding="1em",
        border_bottom="1px solid rgba(255, 255, 255, 0.05)",
        _hover={"bg": "rgba(255, 255, 255, 0.02)"},
    )

# --- 3. MAIN PAGE LAYOUT ---
def index():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.heading("Dashboard Overview", color="white", size="7", margin_bottom="1em"),
            
            rx.grid(
                stats_card("Global Streak", State.streak, "Days Active"),
                stats_card("Completion", State.completion, "Today's Target"),
                stats_card("Active Habits", State.total_habits, "Tracking Now"),
                columns="3",
                spacing="5",
                width="100%",
            ),

            rx.vstack(
                rx.heading("Manage Habits", size="5", color="white", margin_top="2em"),
                
                rx.hstack(
                    rx.input(
                        placeholder="What's your next habit?", 
                        on_change=State.set_new_habit_name,
                        value=State.new_habit_name,
                        bg="rgba(255, 255, 255, 0.05)",
                        border="1px solid #334",
                        color="white",
                        _focus={"border_color": "cyan"},
                        width="400px"
                    ),
                    rx.button(
                        "Create Habit", 
                        on_click=State.add_habit, 
                        bg="cyan", 
                        color="black",
                        _hover={"bg": "#00e5ff"}
                    ),
                    spacing="4",
                    padding_y="1em"
                ),

                rx.vstack(
                    rx.foreach(State.habits, habit_item),
                    width="100%",
                    bg="rgba(18, 25, 45, 0.5)",
                    border_radius="12px",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    padding="1em",
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

app = rx.App()
app.add_page(index, on_load=State.on_load)