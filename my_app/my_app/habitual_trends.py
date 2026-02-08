import reflex as rx
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- 1. SETUP ---
# Load environment variables (for local dev)
load_dotenv()

# Configure Gemini API
# Note: On Reflex Cloud, set this via 'reflex cloud secrets set GOOGLE_API_KEY ...'
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# --- 2. STATE ---
class TrendState(rx.State):
    # Navigation State
    current_view: str = "Overview"

    # User Data
    streak: int = 14
    mood: int = 88
    completion: int = 95
    
    # Journal Data
    journal_entry: str = ""
    saved_entries: list[str] = []

    # AI Data
    ai_response: str = ""
    is_loading: bool = False

    def set_view(self, view_name: str):
        self.current_view = view_name

    def set_journal_entry(self, text: str):
        self.journal_entry = text

    def save_journal(self):
        if self.journal_entry:
            self.saved_entries.append(self.journal_entry)
            self.journal_entry = "" # Clear input

    async def ask_ai(self):
        self.is_loading = True
        yield
        try:
            # Check if API key is present
            if not api_key:
                self.ai_response = "Error: Google API Key not found. Please set GOOGLE_API_KEY in secrets."
            else:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = (
                    f"User Data: Streak {self.streak} days, Mood {self.mood}/100. "
                    "Give me 3 short, punchy, elite-performance habits."
                )
                response = model.generate_content(prompt)
                self.ai_response = response.text
        except Exception as e:
            self.ai_response = f"Connection Error: {str(e)}"
        self.is_loading = False

# --- 3. UI COMPONENTS ---

def sidebar_item(label: str, icon: str, target_view: str):
    """A button that switches the current view."""
    return rx.hstack(
        rx.icon(icon, size=20, color=rx.cond(TrendState.current_view == target_view, "white", "gray")),
        rx.text(label, size="3", weight="bold", color=rx.cond(TrendState.current_view == target_view, "white", "gray")),
        padding="12px",
        border_radius="10px",
        cursor="pointer",
        bg=rx.cond(TrendState.current_view == target_view, "rgba(255,255,255,0.1)", "transparent"),
        _hover={"bg": "rgba(255,255,255,0.05)"},
        width="100%",
        align="center",
        on_click=TrendState.set_view(target_view)
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
        width="100%",
        min_width="250px",
    )

# --- 4. VIEW CONTENT (The Different Pages) ---

def overview_view():
    return rx.vstack(
        rx.heading("Dashboard Overview", size="8", color="white"),
        rx.text("Your command center is ready.", color="gray"),
        rx.spacer(height="2em"),
        rx.grid(
            stat_card("Current Streak", f"{TrendState.streak} Days", "flame", "orange"),
            stat_card("Mental Clarity", f"{TrendState.mood}%", "brain", "blue"),
            stat_card("Habit Completion", f"{TrendState.completion}%", "target", "green"),
            columns=rx.breakpoints(initial="1", sm="3"), 
            spacing="4",
            width="100%",
        ),
        rx.spacer(height="2em"),
        rx.box(
            rx.vstack(
                rx.heading("AI Performance Coach", size="4", color="white"),
                rx.button(
                    "Generate Insights", 
                    on_click=TrendState.ask_ai, 
                    loading=TrendState.is_loading, 
                    color_scheme="plum", 
                    variant="soft",
                    width="100%",
                ),
                rx.divider(margin_y="1em", color_scheme="gray"),
                rx.cond(
                    TrendState.ai_response != "",
                    rx.markdown(TrendState.ai_response, color="white"),
                    rx.text("Tap button for analysis...", color="gray"),
                ),
            ),
            padding="24px",
            bg="rgba(20, 20, 30, 0.6)",
            border="1px solid rgba(217, 70, 239, 0.2)",
            border_radius="16px",
            width="100%",
        ),
        width="100%"
    )

def journal_view():
    return rx.vstack(
        rx.heading("Daily Journal", size="8", color="white"),
        rx.text("Capture your thoughts and wins.", color="gray"),
        rx.spacer(height="2em"),
        rx.text_area(
            placeholder="What did you achieve today?",
            value=TrendState.journal_entry,
            on_change=TrendState.set_journal_entry,
            min_height="200px",
            bg="rgba(255,255,255,0.05)",
            color="white",
        ),
        rx.button("Save Entry", on_click=TrendState.save_journal, color_scheme="plum"),
        rx.divider(margin_y="2em", color_scheme="gray"),
        rx.heading("Recent Entries", size="4", color="white"),
        rx.foreach(
            TrendState.saved_entries,
            lambda entry: rx.card(rx.text(entry, color="white"), bg="rgba(255,255,255,0.03)", margin_bottom="1em", width="100%")
        ),
        width="100%"
    )

def analytics_view():
    return rx.vstack(
        rx.heading("Performance Analytics", size="8", color="white"),
        rx.text("Deep dive into your data.", color="gray"),
        rx.spacer(height="2em"),
        # Simulated Charts using Progress Bars
        rx.card(
            rx.vstack(
                rx.text("Focus Consistency", color="white", weight="bold"),
                rx.progress(value=80, color_scheme="blue", height="10px"),
                rx.text("Sleep Quality", color="white", weight="bold", margin_top="1em"),
                rx.progress(value=65, color_scheme="purple", height="10px"),
                rx.text("Hydration Goal", color="white", weight="bold", margin_top="1em"),
                rx.progress(value=90, color_scheme="cyan", height="10px"),
                width="100%",
            ),
            bg="rgba(255,255,255,0.03)",
            width="100%"
        ),
        width="100%"
    )

# --- 5. MAIN LAYOUT ---
def index():
    return rx.hstack(
        # -- LEFT SIDEBAR --
        rx.vstack(
            rx.heading("PRO DASHBOARD", size="6", weight="bold", color="white"),
            rx.text("HABITUAL TRENDS", size="1", color="gray", letter_spacing="2px"),
            rx.spacer(height="2em"),
            rx.vstack(
                # WIRED UP BUTTONS
                sidebar_item("Overview", "layout-dashboard", "Overview"),
                sidebar_item("Journal", "book-open", "Journal"),
                sidebar_item("Analytics", "bar-chart-2", "Analytics"),
                spacing="2",
                width="100%",
            ),
            rx.spacer(),
            rx.text("Graham B.", size="2", color="gray"),
            width="280px",
            height="100vh",
            padding="2em",
            bg="#0f1115", 
            border_right="1px solid rgba(255,255,255,0.05)",
            display=["none", "none", "flex"],
        ),

        # -- RIGHT CONTENT --
        rx.box(
            rx.vstack(
                # Mobile Header
                rx.hstack(
                    rx.heading("HABITUAL", size="5", color="white"),
                    rx.spacer(),
                    # Mobile Menu Items (Simple version for phone)
                    rx.menu.root(
                        rx.menu.trigger(rx.icon("menu", color="white")),
                        rx.menu.content(
                            rx.menu.item("Overview", on_click=TrendState.set_view("Overview")),
                            rx.menu.item("Journal", on_click=TrendState.set_view("Journal")),
                            rx.menu.item("Analytics", on_click=TrendState.set_view("Analytics")),
                        ),
                    ),
                    width="100%",
                    display=["flex", "flex", "none"],
                    padding_bottom="1em",
                ),

                # DYNAMIC CONTENT SWITCHER
                rx.match(
                    TrendState.current_view,
                    ("Overview", overview_view()),
                    ("Journal", journal_view()),
                    ("Analytics", analytics_view()),
                    overview_view() # Fallback
                ),
                
                padding=["1.5em", "3em"],
                max_width="1200px",
            ),
            width="100%",
            height="100vh",
            bg="#000000",
            overflow_y="auto",
        ),
        spacing="0",
        width="100%",
    )

# --- 6. APP DEFINITION ---
app = rx.App(theme=rx.theme(appearance="dark", accent_color="plum", radius="large"))
app.add_page(index, route="/", title="Habitual Trends | PRO")