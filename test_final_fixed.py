import os
import opik
from opik import track
from google import genai

# 1. SETUP KEYS
# We get Opik key from the environment variable you just set
opik_key = os.environ.get("OPIK_API_KEY")
if not opik_key:
    print("? Error: OPIK_API_KEY is missing. Please run $env:OPIK_API_KEY = 'YOUR_KEY'")
    exit()

# Configure Opik
opik.configure(api_key=opik_key, workspace="habitual-trends-health")

# Configure Gemini (Using the key you provided earlier)
GEMINI_KEY = "AIzaSyA-kVfYYHIg_oPJlD8IromotoPMPpQQmVU"
client = genai.Client(api_key=GEMINI_KEY)

# 2. APP LOGIC
USER_CONTEXT = {
    "user_email": "graham@habitual.com",
    "recent_logs": [
        {"habit": "Morning Run", "status": "skipped", "date": "2026-02-05"},
        {"habit": "Drink Water", "status": "completed", "date": "2026-02-05"},
    ]
}

@track(name="habit_insight_gemini_2_5")
def generate_insight(user_data):
    print(f"?? Asking Gemini 2.5 Flash for insight on {user_data['user_email']}...")
    
    prompt = f"""
    You are an AI coach for the 'Habitual Trends' app.
    Analyze these logs: {user_data['recent_logs']}
    Give a short, punchy motivational tip.
    """

    # Using Gemini 2.5 Flash
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text

if __name__ == "__main__":
    try:
        print("?? Sending request...")
        result = generate_insight(USER_CONTEXT)
        print("\n? Gemini Response:")
        print(f"\"{result}\"")
        print("\n? Check your Opik Dashboard for 'habit_insight_gemini_2_5'!")
    except Exception as e:
        print(f"\n? Error: {e}")
