import opik
from opik import track

# Initialize configuration
opik.configure()

@track
def analyze_habit_trends(user_data):
    # Your LLM logic here
    result = "User habit: consistent morning exercise."
    return result

# Calling the function automatically sends a trace to Opik
analyze_habit_trends({"user_id": 123, "days": 30})
