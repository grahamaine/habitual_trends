import os
from opik import track
from opik.integrations.openai import track_openai
from openai import OpenAI

# 1. Initialize OpenAI with Opik tracking
# Make sure OPENAI_API_KEY is set in your environment variables
openai_client = OpenAI()
track_openai(openai_client)

# Mock Data for Graham
USER_CONTEXT = {
    "user_email": "graham@habitual.com",
    "recent_logs": [
        {"habit": "Morning Run", "status": "skipped", "date": "2023-10-24"},
        {"habit": "Drink 2L Water", "status": "completed", "date": "2023-10-24"},
        {"habit": "Read 30 mins", "status": "completed", "date": "2023-10-24"},
        {"habit": "Morning Run", "status": "skipped", "date": "2023-10-25"},
    ]
}

@track(name="generate_habit_insight")
def generate_insight(user_data):
    """
    Generates a motivational insight based on habit history.
    """
    
    # Construct the prompt
    prompt = f"""
    You are an AI coach for the 'Habitual Trends' app.
    Analyze the following user data for {user_data['user_email']}:
    {user_data['recent_logs']}
    
    Provide a concise, 1-sentence insight or encouragement. 
    Focus on patterns (e.g., skipping runs).
    """

    print(f"🤖 Generating insight for {user_data['user_email']}...")

    # Call LLM
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini", # or your preferred model
        messages=[
            {"role": "system", "content": "You are a helpful habit tracking assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    insight = response.choices[0].message.content
    return insight

if __name__ == "__main__":
    # Run the generation
    try:
        result = generate_insight(USER_CONTEXT)
        print("\n✅ LLM Response Received:")
        print(f"\"{result}\"")
        print("\n🚀 Check your Opik Dashboard (habitual_trends project) to see the trace!")
    except Exception as e:
        print(f"❌ Error: {e}")