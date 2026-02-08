import os
from google import genai
from opik import track
from opik.integrations.genai import track_genai
from dotenv import load_dotenv

# 1. Load your .env file
load_dotenv()

# 2. Configure Opik Project
os.environ["OPIK_PROJECT_NAME"] = "habitual_trends"

# 3. Initialize tracked Gemini client
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
gemini_client = track_genai(client)

@track
def test_habit_analysis(habit_name):
    """A test function to simulate your app logic."""
    prompt = f"Provide a one-sentence health tip for someone trying to improve their {habit_name}."
    
    # This call is automatically tracked by track_genai
    response = gemini_client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    import opik # Make sure it's imported at the top too
    print("🚀 Running Habitual Trends Verification...")
    try:
        result = test_habit_analysis("sleep consistency")
        print(f"\nGemini Response: {result}")
        
        # --- THE CRITICAL FIX ---
        print("\n⏳ Flushing traces to Opik...")
        opik.flush() 
        # ------------------------
        
        print("\n✅ Success! Refresh your dashboard at Comet.com")
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")