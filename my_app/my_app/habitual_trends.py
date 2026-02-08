import reflex as rx
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- 1. SETUP & CONFIG ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# --- 2. THE BRAIN (State) ---
class TrendState(rx.State):
    streak: int = 14
    mood: int = 88
    completion: int = 95
    ai_response: str = ""
    is_loading: bool = False

    def ask_ai(self):
        self.is_loading = True
        yield
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = (
                f"User Data: Streak {self.streak} days, Mood {self.mood}/100. "
                "Give me 3 short, punchy, elite-performance habits to add next."
            )
            response = model.generate_content(prompt)
            self.ai_response = response.text
        except Exception as e:
            self.ai_response = "AI Connection Error. Check API Key."
        self.is_loading = False

# --- 3. UI COMPONENTS ---
def sidebar_item(label: str, icon: str, active: bool = False):
    return rx.hstack(
        rx.icon(icon, size=20, color="white" if active else "gray"),
        rx.text(label, size="3", weight="bold" if active else "medium", color="white" if active else "gray"),
        padding="12px",
        border_radius="10px",
        cursor="pointer",
        bg="rgba(255,255,255,0.1)" if active else "transparent",
        _hover={"bg": "rgba(255,255,255,0.05)"},
        width="100%",
        align="center",
    )

def stat_card(title: str, value: str, icon: str, color: str):
    return rx.box(
        rx.hstack(
            rx.center(
                rx.icon(icon, size=24, color="white"),
                bg=f"var(--{color}-9)",
                padding="12px",
                border_radius="12px",
            ),
            rx.vstack(
                rx.text(title, size="1", color="gray", weight="bold"),
                rx.heading(value, size="6", color="white"),
                spacing="1",
            ),
            spacing="4",
            align="center",
        ),
        padding="20px",
        bg="rgba(255,255,255,0.03)",
        border="1px solid rgba(255,255,255,0.05)",
        border_radius="16px",
    )

def ai_section():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("sparkles", color="#D946EF", size=24), # Fuschia color
                rx.heading("AI Performance Coach", size="4", color="white"),
                rx.spacer(),
                rx.button(
                    "Generate Insights",
                    on_click=TrendState.ask_ai,
                    loading=TrendState.is_loading,
                    color_scheme="plum",
                    variant="soft",
                ),
                width="100%",
                align="center",
            ),
            rx.divider(margin_y="1em", color_scheme="gray"),
            rx.cond(
                TrendState.ai_response != "",
                rx.markdown(TrendState.ai_response, color="white"),
                rx.text("Tap the button to analyze your trends...", color="gray", style={"font_style": "italic"}),
            ),
        ),
        padding="24px",
        bg="rgba(20, 20, 30, 0.6)",
        border="1px solid rgba(217, 70, 239, 0.2)", # Subtle purple border
        border_radius="16px",
        width="100%",
    )

# --- 4. MAIN LAYOUT ---
def index():
    return rx.hstack(
        # -- LEFT SIDEBAR --
        rx.vstack(
            rx.heading("HABITUAL", size="6", font_weight="900", color="white", letter_spacing="-1px"),
            rx.text("TRENDS", size="1", color="gray", letter_spacing="2px"),
            rx.spacer(height="2em"),
            rx.vstack(
                sidebar_item("Dashboard", "layout-dashboard", active=True),
                sidebar_item("Journal", "book-open"),
                sidebar_item("Analytics", "bar-chart-2"),
                sidebar_item("Settings", "settings"),
                spacing="2",
                width="100%",
            ),
            rx.spacer(),
            rx.hstack(
                rx.avatar(fallback="GB", size="3", radius="full", color_scheme="plum"),
                rx.vstack(
                    rx.text("Graham B.", size="2", weight="bold", color="white"),
                    rx.text("Pro Plan", size="1", color="gray"),
                    spacing="0",
                ),
                padding="1em",
                bg="rgba(255,255,255,0.03)",
                border_radius="12px",
                width="100%",
                align="center",
            ),
            width="280px",
            height="100vh",
            padding="2em",
            bg="#0f1115", # Very dark sidebar
            border_right="1px solid rgba(255,255,255,0.05)",
            display=["none", "none", "flex"], # Hidden on mobile
        ),

        # -- RIGHT CONTENT --
        rx.box(
            rx.vstack(
                rx.heading("Overview", size="8", color="white"),
                rx.text("Welcome back to your command center.", color="gray"),
                rx.spacer(height="2em"),
                
                # Stats Grid
                rx.grid(
                    stat_card("Current Streak", f"{TrendState.streak} Days", "flame", "orange"),
                    stat_card("Mental Clarity", f"{TrendState.mood}%", "brain", "blue"),
                    stat_card("Habit Completion", f"{TrendState.completion}%", "target", "green"),
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
                
                rx.spacer(height="2em"),
                
                # AI Section
                ai_section(),
                
                padding="3em",
                max_width="1200px",
                width="100%",
            ),
            width="100%",
            height="100vh",
            bg="#000000", # Pure black background
            overflow_y="auto",
        ),
        spacing="0",
        width="100%",
    )

# --- 5. APP DEFINITION ---
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="plum",
        radius="large",
    )
)
app.add_page(index, route="/", title="Habitual Trends | Pro")