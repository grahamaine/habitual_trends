import os
from google import genai

# This retrieves the key from your Lenovo system, NOT from the file
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))