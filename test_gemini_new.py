from google import genai
from opik import track

# 1. Setup the Client
# We use your new key directly to override any conflicting environment variables
client = genai.Client(api_key="AIzaSyA-kVfYYHIg_oPJlD8IromotoPMPpQQmVU")

# Mock User Data
USER_CONTEXT = {
    "user_email": "graham@habitual.com",
    "recent_logs": [
        {"habit": "Morning Run", "status": "skipped", "date": "2023-10-24"},
        {"habit": "Drink 2L Water", "status": "completed", "date": "2023-10-24"},
    ]
}

@track(name="habit_insight_gemini_v2")
def generate_insight(user_data):
    print(f"?? Asking Gemini for insight on {user_data['user_email']}...")
    
    prompt = f"""
    You are an AI coach for the 'Habitual Trends' app.
    Analyze these logs: {user_data['recent_logs']}
    Give a short motivational tip.
    """

    # Call the model
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    
    return response.text

if __name__ == "__main__":
    try:
        print("?? Sending request to Gemini...")
        result = generate_insight(USER_CONTEXT)
        print("\n? Gemini Response:")
        print(f"\"{result}\"")
        print("\n? Check your Opik Dashboard for the trace!")
    except Exception as e:
        print(f"\n? Error: {e}")
