import reflex as rx

# --- 1. STATE & LOGIC ---
class State(rx.State):
    """The app state."""
    # Login Credentials
    email: str = ""
    password: str = ""

    # Dashboard Stats (Now variables, not hardcoded)
    streak: int = 12
    completion: str = "85%"
    total_habits: int = 5

    def handle_login(self):
        """Prints credentials to the terminal (Backend Logic would go here)."""
        print(f"Attempting Login with -> Email: {self.email}, Password: {self.password}")
        # In the future, you would send a request to your Rust backend here.

    def increase_streak(self):
        """A test function to show the stats are 'alive'."""
        self.streak += 1

# --- 2. UI COMPONENTS ---

def stats_card(title: str, value: str, subtext: str):
    """A reusable glass-morphism card for the top stats."""
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
        # -- Logo --
        rx.vstack(
            rx.icon(tag="activity", color="cyan", size=40),
            rx.heading("HABITUAL TRENDS", size="4", color="cyan", letter_spacing="2px"),
            rx.text("AI AGENT", size="1", color="white", letter_spacing="4px"),
            align_items="center",
            spacing="1",
            padding_bottom="3em",
        ),
        
        # -- Login Form (Connected to State) --
        rx.vstack(
            rx.input(
                placeholder="Email", 
                on_change=State.set_email,  # Updates State.email
                bg="transparent", border="1px solid #334", color="white"
            ),
            rx.input(
                placeholder="Password", 
                type="password", 
                on_change=State.set_password, # Updates State.password
                bg="transparent", border="1px solid #334", color="white"
            ),
            rx.link("Forgot Password?", color="gray", font_size="0.8em", align_self="end"),
            
            rx.button(
                "Login", 
                on_click=State.handle_login, # Triggers the print function
                bg="linear-gradient(90deg, #00f0ff, #0077ff)", 
                color="black", 
                width="100%",
                _hover={"opacity": 0.8}
            ),
            # Added a test button to prove stats are real
            rx.button(
                "Test: Add Streak +1", 
                on_click=State.increase_streak,
                variant="outline", 
                color="cyan", 
                border_color="cyan", 
                width="100%",
                font_size="0.8em"
            ),
            spacing="4",
            width="100%",
            padding_bottom="3em",
        ),

        # -- Navigation --
        rx.vstack(
            rx.hstack(rx.icon(tag="layout_dashboard", color="cyan"), rx.text("Dashboard", color="white"), spacing="3", cursor="pointer"),
            rx.hstack(rx.icon(tag="bar_chart_2", color="cyan"), rx.text("Analytics", color="white"), spacing="3", cursor="pointer"),
            rx.hstack(rx.icon(tag="settings", color="cyan"), rx.text("Settings", color="white"), spacing="3", cursor="pointer"),
            align_items="start",
            spacing="6",
            width="100%"
        ),

        bg="#0B1120",
        height="100vh",
        width="350px",
        padding="2em",
        align_items="center",
        border_right="1px solid #1f2937",
        display=["none", "none", "flex", "flex"],
    )

# --- 3. MAIN PAGE ---
def index():
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.heading("Welcome back, Graham", color="white", size="8", margin_bottom="1em"),
            
            # The Stats Row (Now connected to State)
            rx.grid(
                stats_card("Current Streak", State.streak, "Days in a row"),
                stats_card("Completion", State.completion, "All tasks done"),
                stats_card("Total Habits", State.total_habits, "Active habits"),
                columns="3",
                spacing="5",
                width="100%",
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
    )

app = rx.App()
app.add_page(index)