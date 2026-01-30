import reflex as rx
import httpx

# --- 1. STATE & LOGIC ---
class State(rx.State):
    """The app state."""
    email: str = ""
    password: str = ""
    streak: int = 12
    completion: str = "85%"
    total_habits: int = 5
    
    # List of habits fetched from Rust
    habits: list[dict] = []

    def set_email(self, value: str):
        self.email = value
    def set_password(self, value: str):
        self.password = value

    async def handle_login(self):
        print(f"Logging in user: {self.email}")
        async with httpx.AsyncClient() as client:
            try:
                # Talking to Rust on Port 8080
                response = await client.post(
                    "http://localhost:8080/api/login", 
                    json={"email": self.email, "password": self.password}
                )
                
                if response.status_code == 200:
                    print("✅ Login Success! Redirecting...")
                    return rx.redirect("/dashboard")
                else:
                    print(f"❌ Login Failed: {response.text}")
                    return rx.window_alert("Login Failed")

            except Exception as e:
                print(f"⚠️ Connection Error: {e}")
                return rx.window_alert("Cannot connect to server.")

    async def load_data(self):
        print("Fetching habits from Rust...")
        async with httpx.AsyncClient() as client:
            try:
                res = await client.get("http://localhost:8080/api/habits")
                
                if res.status_code == 200:
                    self.habits = res.json()
                    print("Received habits:", self.habits)
                else:
                    print("Failed to get habits")
            except Exception as e:
                print(f"Error fetching data: {e}")

    def increase_streak(self):
        self.streak += 1

# --- 2. UI COMPONENTS ---

def stats_card(title: str, value: str, subtext: str):
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
        box_shadow="0 4px 30px rgba(0, 0, 0, 0.5)",
    )

def habit_row(habit: dict):
    """Draws a single row for a habit."""
    return rx.hstack(
        # --- FIX IS HERE: Used rx.cond instead of python if/else ---
        rx.icon(
            tag="check_circle", 
            color=rx.cond(habit["completed"], "cyan", "gray")
        ),
        # -----------------------------------------------------------
        rx.text(habit["name"], color="white", font_size="1.1em", weight="bold"),
        rx.spacer(),
        rx.text(f"Streak: {habit['streak']} 🔥", color="orange"),
        
        bg="rgba(255, 255, 255, 0.05)",
        padding="1em",
        border_radius="10px",
        width="100%",
        align_items="center",
        border="1px solid rgba(255, 255, 255, 0.1)"
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
            rx.hstack(rx.icon(tag="layout_dashboard", color="cyan"), rx.text("Dashboard", color="white"), spacing="3", cursor="pointer"),
            rx.hstack(rx.icon(tag="bar_chart_2", color="cyan"), rx.text("Analytics", color="white"), spacing="3", cursor="pointer"),
            rx.hstack(rx.icon(tag="settings", color="cyan"), rx.text("Settings", color="white"), spacing="3", cursor="pointer"),
            align_items="start",
            spacing="6",
            width="100%"
        ),

        rx.box(
            rx.link("Log Out", href="/", color="gray", font_size="0.9em"),
            margin_top="auto", 
            padding_top="2em"
        ),

        bg="#0B1120",
        height="100vh",
        width="250px",
        padding="2em",
        align_items="center",
        border_right="1px solid #1f2937",
        display=["none", "none", "flex", "flex"],
    )

# --- 3. PAGES ---

def login_page():
    return rx.center(
        rx.vstack(
            rx.heading("Welcome Back", color="white", size="8"),
            rx.text("Sign in to access your AI Agent", color="gray", margin_bottom="1em"),
            
            rx.input(placeholder="Email", on_change=State.set_email, width="100%", bg="transparent", border="1px solid #334", color="white"),
            rx.input(placeholder="Password", type="password", on_change=State.set_password, width="100%", bg="transparent", border="1px solid #334", color="white"),
            
            rx.button("Login", on_click=State.handle_login, width="100%", bg="linear-gradient(90deg, #00f0ff, #0077ff)", color="black"),
            
            bg="#0B1120",
            padding="3em",
            border_radius="20px",
            border="1px solid #334",
            box_shadow="0 0 20px rgba(0, 240, 255, 0.1)",
            width="400px",
            spacing="4",
        ),
        bg="black",
        height="100vh",
        width="100%",
    )

def dashboard_page():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.heading("Dashboard", color="white", size="8", margin_bottom="1em"),
            
            # Stats Grid
            rx.grid(
                stats_card("Current Streak", State.streak, "Days in a row"),
                stats_card("Completion", State.completion, "All tasks done"),
                stats_card("Total Habits", State.total_habits, "Active habits"),
                columns="3",
                spacing="5",
                width="100%",
            ),
            
            rx.separator(color_scheme="gray", margin_y="1em"),
            rx.heading("Your Habits", color="white", size="6"),

            # THE HABIT LIST
            rx.vstack(
                rx.foreach(State.habits, habit_row),
                width="100%",
                spacing="3"
            ),
            
            bg_image="url('/dashboard_bg.jpg')",
            bg_size="cover",
            bg_position="center",
            width="100%",
            height="100vh",
            padding="3em",
            spacing="5",
        ),
        spacing="0",
        bg="black",
        on_mount=State.load_data 
    )

app = rx.App()
app.add_page(login_page, route="/")
app.add_page(dashboard_page, route="/dashboard")