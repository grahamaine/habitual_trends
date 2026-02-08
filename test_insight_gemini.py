import os
import google.generativeai as genai
from opik import track

# Check for API Key
if "GOOGLE_API_KEY" not in os.environ:
    print("? Error: GOOGLE_API_KEY not found in environment variables.")
    print("Please run: $env:GOOGLE_API_KEY = 'YOUR_KEY'")
    exit()

# 1. Configure Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Mock User Data
USER_CONTEXT = {
    "user_email": "graham@habitual.com",
    "recent_logs": [
        {"habit": "Morning Run", "status": "skipped", "date": "2023-10-24"},
        {"habit": "Drink 2L Water", "status": "completed", "date": "2023-10-24"},
        {"habit": "Morning Run", "status": "skipped", "date": "2023-10-25"},
    ]
}

# 2. Add Opik Tracking
@track(name="generate_habit_insight_gemini")
def generate_insight(user_data):
    print(f"?? Asking Gemini for insight on {user_data['user_email']}...")
    
    prompt = f"""
    You are an AI coach for the 'Habitual Trends' app.
    Analyze these logs: {user_data['recent_logs']}
    
    Give a one-sentence motivational tip based on the skipped runs.
    """

    # Call Gemini
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    try:
        print("?? Sending request to Google Gemini...")
        result = generate_insight(USER_CONTEXT)
        
        print("\n? Gemini Response:")
        print(f"\"{result}\"")
        print("\n? Check your Opik Dashboard (habitual-trends-health) for the trace!")
        
    except Exception as e:
        print(f"? Error: {e}")
