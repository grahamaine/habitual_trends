import reflex as rx
import os
from opik import track
from opik.integrations.langchain import OpikTracer
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Initialize Opik and Gemini
# (Consider moving these keys to a .env file later)
os.environ["OPIK_PROJECT_NAME"] = "habitual_trends"
opik_tracer = OpikTracer()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# --- STEP 1: Define the tracked logic OUTSIDE the class ---
@track
async def process_wellness_check(count: int):
    """
    This function handles both the status logic and the AI call.
    The @track decorator logs the entire process to Opik.
    """
    status = "Normal" if count < 10 else "High Activity"
    
    # We call Gemini here. Opik will nest this LLM call under this trace.
    response = await llm.ainvoke(
        f"The user has a {status} wellness count of {count}. Give a 1-sentence tip.",
        config={"callbacks": [opik_tracer]}
    )
    
    return {
        "status": status,
        "tip": response.content
    }

class State(rx.State):
    """The app state for Habitual Trends."""
    count: int = 0
    status_report: str = ""
    ai_response: str = ""
    is_loading: bool = False

    async def run_wellness_flow(self):
        """Triggered by the UI to run the full tracked process."""
        self.is_loading = True
        yield
        
        # Call our tracked function
        result = await process_wellness_check(self.count)
        
        self.status_report = result["status"]
        self.ai_response = result["tip"]
        self.is_loading = False

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Habitual Trends", size="9"),
            rx.text("Track your medical habits and wellness data."),
            
            rx.hstack(
                rx.button("Decrement", on_click=State.decrement, color_scheme="ruby", variant="soft"),
                rx.heading(State.count, size="7"),
                rx.button("Increment", on_click=State.increment, color_scheme="grass", variant="soft"),
                spacing="4",
                align="center",
            ),
            
            rx.divider(),

            rx.button(
                "Run Wellness Check", 
                on_click=State.run_wellness_flow,
                loading=State.is_loading,
                color_scheme="indigo",
            ),

            rx.cond(
                State.status_report != "",
                rx.card(
                    rx.text(f"Status: {State.status_report}", weight="bold"),
                    rx.text(State.ai_response, font_style="italic"),
                    padding="4",
                    width="100%",
                )
            ),
            
            rx.text("System Status: Operational", color_content_hint=True),
            spacing="5",
            align="center",
            text_align="center",
        ),
        height="100vh",
        padding="20px",
    )

app = rx.App()
app.add_page(index, title="Habitual Trends")