import reflex as rx

# 1. STATE (Business Logic)
class State(rx.State):
    """The app state."""
    habits: list[str] = ["Code Rust Backend", "Read AI Papers", "Morning Run"]
    streak: int = 12
    completion_rate: str = "1000%" # Updated to match image

    def add_habit(self):
        """A mock function to add a habit."""
        self.habits.append(f"New Habit {len(self.habits) + 1}")
        self.streak += 1


# 2. COMPONENTS (Reusable UI parts)

# Common style for transparent elements
glass_style = {
    "bg": "rgba(255, 255, 255, 0.05)",
    "backdrop_filter": "blur(12px)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "border_radius": "12px",
}

def sidebar_item(icon: str, text: str):
    """A sidebar navigation link."""
    return rx.hstack(
        rx.icon(icon, color="white", size=20),
        rx.text(text, color="gray.300", size="3", weight="medium"),
        spacing="3",
        padding="0.8em",
        width="100%",
        border_radius="8px",
        _hover={"bg": "rgba(255,255,255,0.1)"},
        cursor="pointer",
    )

def login_sidebar():
    """The left sidebar with login form and nav."""
    return rx.vstack(
        # Logo & Title Area
        rx.vstack(
             # Using a generic icon instead of the specific logo image for simplicity
            rx.icon("hexagon", color=rx.color("cyan", 9), size=40),
            rx.heading("HABITUAL TRENDS", size="3", color="white", letter_spacing="1px"),
            rx.text("AI AGENT", size="2", color="cyan.400", letter_spacing="2px"),
            spacing="1",
            align_items="center",
            margin_bottom="2em",
        ),

        # Login Form Section
        rx.vstack(
            rx.input(
                placeholder="Email",
                bg="rgba(0,0,0,0.3)", border_color="gray.700", color="white"
            ),
            rx.input(
                placeholder="Password", type="password",
                bg="rgba(0,0,0,0.3)", border_color="gray.700", color="white"
            ),
            rx.hstack(
                rx.spacer(),
                rx.link("Forgot Password?", size="1", color="gray.400"),
                width="100%",
            ),
            rx.button(
                "Login", 
                bg="cyan.400", color="black", width="100%", size="3",
                _hover={"bg": "cyan.500"}
            ),
            rx.button(
                "Sign Up", 
                variant="outline", color="white", border_color="gray.600", width="100%", size="3",
                _hover={"bg": "rgba(255,255,255,0.05)"}
            ),
            spacing="3",
            width="100%",
        ),

        rx.divider(margin_y="2em", border_color="gray.700"),

        # Navigation Links
        rx.vstack(
            sidebar_item("layout-dashboard", "Dashboard"),
            sidebar_item("bar-chart-3", "Analytics"),
            sidebar_item("settings", "Settings"),
            spacing="2",
            width="100%",
        ),
        
        # Sidebar container styling
        bg="rgba(0, 9, 20, 0.85)", # Darker semi-transparent background
        backdrop_filter="blur(15px)",
        border_right="1px solid rgba(255,255,255,0.1)",
        padding="2em",
        height="100vh",
        width="300px",
        align_items="center",
    )


def transparent_stat_card(label: str, value: str):
    """The see-through stat cards located at the top."""
    return rx.box(
        rx.vstack(
            rx.text(label, size="2", color="gray.300", weight="medium"),
            rx.heading(value, size="8", color="white", font_weight="bold"),
            align_items="start",
            spacing="1",
        ),
        padding="1.5em",
        width="100%",
        **glass_style # Applies the glass effect defined above
    )

def habit_row(habit_name: str):
    """How each habit looks in the list."""
    return rx.box(
        rx.hstack(
            rx.checkbox(color_scheme="cyan"),
            rx.text(habit_name, size="3", color="white", weight="medium"),
            rx.spacer(),
            # Using an icon for active state instead of a badge for a cleaner look
            rx.icon("activity", color=rx.color("cyan", 9), size=18),
            width="100%",
            align_items="center",
            spacing="4",
        ),
        padding="1em",
        width="100%",
        **glass_style
    )


# 3. PAGE LAYOUT
def index():
    return rx.box(
        rx.hstack(
            login_sidebar(),
            
            # Main Content Area
            rx.vstack(
                # Header Title
                rx.heading("Welcome back, Graham", size="8", color="white", weight="bold"),
                
                # Stats Row (3 cards)
                rx.grid(
                    transparent_stat_card("Current Streak", f"{State.streak}"),
                    transparent_stat_card("Completion", State.completion_rate),
                    transparent_stat_card("Total Habits", "3"),
                    columns="3",
                    spacing="4",
                    width="100%",
                    margin_y="2em",
                ),

                # Habits Section Title
                rx.heading("Your Habits", size="6", color="white", margin_top="1em", margin_bottom="0.5em"),

                # The list of habits generated from State
                rx.vstack(
                    rx.foreach(State.habits, habit_row),
                    spacing="3",
                    width="100%",
                ),

                # Add Button (for testing)
                rx.button(
                    rx.hstack(rx.icon("plus"), rx.text("Add Habit")),
                    on_click=State.add_habit, 
                    variant="outline",
                    color="cyan.400",
                    border_color="cyan.400",
                    margin_top="2em",
                    _hover={"bg": "rgba(0, 255, 255, 0.1)"}
                ),
                
                padding_x="3em",
                padding_y="2em",
                width="100%",
                align_items="start",
            ),
            spacing="0",
            height="100vh",
            align_items="start",
        ),
        # Setting the background image for the entire page
        # Ensure 'dashboard_bg.jpg' is placed in the 'assets' folder.
        bg_image="url('/dashboard_bg.jpg')", 
        bg_size="cover",
        bg_position="center",
        bg_repeat="no-repeat",
        height="100vh",
        width="100vw",
        overflow="hidden" # Prevents double scrollbars
    )


# 4. APP DEFINITION (Dark theme enabled)
app = rx.App(theme=rx.theme(appearance="dark", accent_color="cyan"))
app.add_page(index)