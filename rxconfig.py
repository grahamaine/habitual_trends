import os
import opik
import reflex as rx

# 1. Initialize Environment Variables
os.environ["OPIK_API_KEY"] = "0I6LWPGVaiyAf0O48fDGcT6tC"
os.environ["OPIK_PROJECT_NAME"] = "habitual_trends"
# Added the Google API Key here for Windows compatibility
os.environ["GOOGLE_API_KEY"] = "AIzaSyDT5XFqkvSjo5k5vM1OqOzTw1WHJmOUekI"

opik.configure()

# 2. Reflex Configuration
config = rx.Config(
    app_name="habitual_trends",
    state_auto_setters=True, 
    plugins=[
        rx.plugins.SitemapPlugin(),
    ],
)