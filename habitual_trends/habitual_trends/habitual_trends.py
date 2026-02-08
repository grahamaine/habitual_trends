import reflex as rx
from .frontend import index, TrendState  # Import the UI and Logic

# Define the App
app = rx.App(
    theme=rx.theme(
        appearance="dark", 
        accent_color="plum", 
        radius="large"
    )
)

# Add the page from frontend.py
app.add_page(index, route="/", title="Habitual Trends | PRO")