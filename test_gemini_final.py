from google import genai
from opik import track

# 1. Setup Client with your working key
client = genai.Client(api_key="AIzaSyA-kVfYYHIg_oPJlD8IromotoPMPpQQmVU")

# Mock User Data
USER_CONTEXT = {
    "user_email": "graham@habitual.com",
    "recent_logs": [
        {"habit": "Morning Run", "status": "skipped", "date": "2026-02-05"},
        {"habit": "Drink 2L Water", "status": "completed", "date": "2026-02-05"},
    ]
}

@track(name="habit_insight_gemini_2_0")
def generate_insight(user_data):
    print(f"?? Asking Gemini 2.0 Flash for insight on {user_data['user_email']}...")
    
    prompt = f"""
    You are an AI coach for the 'Habitual Trends' app.
    Analyze these logs: {user_data['recent_logs']}
    Give a short, punchy motivational tip.
    """

    # 2. Call the CORRECT model name
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    return response.text

if __name__ == "__main__":
    try:
        print("?? Sending request...")
        result = generate_insight(USER_CONTEXT)
        print("\n? Gemini Response:")
        print(f"\"{result}\"")
        print("\n? Check your Opik Dashboard for 'habit_insight_gemini_2_0'!")
    except Exception as e:
        print(f"\n? Error: {e}")
