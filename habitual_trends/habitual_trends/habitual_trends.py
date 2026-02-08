import reflex as rx
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- 1. CONFIGURATION ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# --- 2. STATE MANAGEMENT (The "Brain") ---
class TrendState(rx.State):
    analysis: str = ""
    is_loading: bool = False

    def get_insights(self, habit_data: list[str]):
        self.is_loading = True
        yield  # Show the loading spinner immediately
        
        try:
            # Using the fast flash model for real-time wellness insights
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = (
                f"As a health and wellness expert, analyze these habits: {habit_data}. "
                "Provide 3 actionable trends or suggestions for improvement in markdown format."
            )
            response = model.generate_content(prompt)
            self.analysis = response.text
        except Exception as e:
            self.analysis = f"Error: Could not reach the wellness AI. {str(e)}"
        
        self.is_loading = False

# --- 3. UI COMPONENTS (The "Body") ---
def trend_dashboard() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Habitual Insights", size="8", margin_bottom="0.5em"),
            rx.text("AI-powered analysis of your daily routines", color_alpha="0.7"),
            
            rx.button(
                "Generate Trend Analysis",
                on_click=TrendState.get_insights(["8 hours sleep", "2L water", "No exercise"]),
                loading=TrendState.is_loading,
                color_scheme="teal",
                size="3",
                padding="1.5em",
            ),
            
            rx.cond(
                TrendState.analysis != "",
                rx.card(
                    rx.markdown(TrendState.analysis),
                    width="100%",
                    margin_top="2em",
                    padding="1.5em",
                    box_shadow="lg",
                ),
            ),
            spacing="5",
            align="center",
            width="100%",
            max_width="600px",
        ),
        padding_top="10vh",
        width="100%",
    )

# --- 4. APP INITIALIZATION (The "Entry Point") ---
# IMPORTANT: These lines must be at the global level for deployment to work
app = rx.App()
app.add_page(trend_dashboard, route="/", title="Habitual Trends | AI Insights")