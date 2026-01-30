import reflex as rx
import httpx  # Required for connecting to your Rust backend

# --- 1. STATE & LOGIC ---
class State(rx.State):
    """The app state."""
    # Login Credentials
    email: str = ""
    password: str = ""

    # Dashboard Stats
    streak: int = 12
    completion: str = "85%"
    total_habits: int = 5

    # LOGIN LOGIC: Connects to your Rust backend
    async def handle_login(self):
        print(f"Sending login request for: {self.email}")
        
        async with httpx.AsyncClient() as client:
            try:
                # This talks to your Rust 'main.rs' running on port 8080
                response = await client.post(
                    "http://localhost:8080/api/login", 
                    json={
                        "email": self.email, 
                        "password": self.password
                    }
                )
                
                if response.status_code == 200:
                    print("✅ Success! Backend replied:", response.json())
                    # You could add a redirect here later: return rx.redirect("/dashboard")
                else:
                    print(f"❌ Failed. Status: {response.status_code}")
                    print("Reason:", response.text)

            except Exception as e:
                print(f"⚠️ Connection Error. Is 'cargo run' active? \nDetails: {e}")

    def increase_streak(self):
        """A test function to show the stats are 'alive'."""
        self.streak += 1

# --- 2. UI COMPONENTS (Helper Functions) ---

def stats_card(title: str, value: str, subtext: str):
    """A reusable glass-morphism card for the top stats."""
    return rx.vstack(
        rx.text(title, color="#a0aec0", font_size="0.9em", font_weight="bold"),
        rx.text(value, color="cyan", font_size="2em", font_weight="bold"),
        rx.text(subtext, color="white", font_size="0.8em"),
        bg="rgba(18, 25, 45, 0.8)", # Semi-transparent dark blue
        backdrop_filter="blur(10px)", # The "Glass" blur effect
        padding="1.5em",
        border_radius="15px",
        border="1px solid rgba(255, 255, 255, 0.1)",
        width="100%",
        align_items="start",
        box_shadow="0 4px 30px rgba(0, 0, 0, 0.5)",
    )

def sidebar():
    """The left-hand navigation sidebar."""
    return rx.vstack(
        # -- Logo Area --
        rx.vstack(
            rx.icon(tag="activity", color="cyan", size=40),
            rx.heading("HABITUAL TRENDS", size="4", color="cyan", letter_spacing="2px"),
            rx.text("AI AGENT", size="1", color="white", letter_spacing="4px"),
            align_items="center",
            spacing="1",
            padding_bottom="3em",
        ),
        
        # -- Login Form --
        rx.vstack(
            rx.input(
                placeholder="Email", 
                on_change=State.set_email, 
                bg="transparent", border="1px solid #334", color="white"
            ),
            rx.input(
                placeholder="Password", 
                type="password", 
                on_change=State.set_password, 
                bg="transparent", border="1px solid #334", color="white"
            ),
            rx.link("Forgot Password?", color="gray", font_size="0.8em", align_self="end"),
            
            rx.button(
                "Login", 
                on_click=State.handle_login, # Calls the Rust API
                bg="linear-gradient(90deg, #00f0ff, #0077ff)", 
                color="black", 
                width="100%",
                _hover={"opacity": 0.8}
            ),
            # Test Button
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

        # -- Navigation Menu --
        rx.vstack(
            rx.hstack(rx.icon(tag="layout_dashboard", color="cyan"), rx.text("Dashboard", color="white"), spacing="3", cursor="pointer"),
            rx.hstack(rx.icon(tag="bar_chart_2", color="cyan"), rx.text("Analytics", color="white"), spacing="3", cursor="pointer"),
            rx.hstack(rx.icon(tag="settings", color="cyan"), rx.text("Settings", color="white"), spacing="3", cursor="pointer"),
            align_items="start",
            spacing="6",
            width="100%"
        ),

        # Sidebar Styling
        bg="#0B1120", # Deep dark navy
        height="100vh",
        width="350px",
        padding="2em",
        align_items="center",
        border_right="1px solid #1f2937",
        display=["none", "none", "flex", "flex"], # Responsive: Hide on mobile
    )

# --- 3. MAIN PAGE LAYOUT ---
def index():
    return rx.hstack(
        # 1. The Sidebar
        sidebar(),

        # 2. The Main Content (With Background Image)
        rx.vstack(
            # Header Text
            rx.heading("Welcome back, Graham", color="white", size="8", margin_bottom="1em"),
            
            # The Stats Row
            rx.grid(
                stats_card("Current Streak", State.streak, "Days in a row"),
                stats_card("Completion", State.completion, "All tasks done"),
                stats_card("Total Habits", State.total_habits, "Active habits"),
                columns="3",
                spacing="5",
                width="100%",
            ),

            # Main Background Styling
            bg_image="url('/dashboard_bg.jpg')", # Ensure this file is in your 'assets' folder
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