from opik import track
import time

# MOCK User Data
USER_CONTEXT = "graham@habitual.com"

# This decorator sends the trace to Opik
@track(name="generate_habit_insight_mock")
def mock_generate_insight(user_email):
    print(f"🤖 Simulating AI generation for {user_email}...")
    time.sleep(1) 
    return "Keep up the good work! (This is a mock response)"

if __name__ == "__main__":
    try:
        print("🚀 Testing Opik connection...")
        result = mock_generate_insight(USER_CONTEXT)
        print("✅ Done! Check your Opik Dashboard.")
    except Exception as e:
        print(f"❌ Error: {e}")