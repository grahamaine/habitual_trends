import requests
import json
import time

# MUST match the port in your Rust code
# Change this line in your client script
BASE_URL = "http://127.0.0.1:3005" 

def get_trends(username):
    url = f"{BASE_URL}/api/trends/{username}"
    # ... rest of your code ...

def log_habit(username, habit_name):
    url = f"{BASE_URL}/api/habits"
    payload = {"user": username, "habit_name": habit_name}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            print(f"✅ Successfully logged '{habit_name}' for {username}")
        else:
            print(f"❌ Failed to log. Status: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

def get_trends(username):
    url = f"{BASE_URL}/api/trends/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            habits = response.json()
            # Ensure habits is a list before looping
            if isinstance(habits, list):
                print(f"\n--- Trends for {username} ---")
                for h in habits:
                    # Using .get() prevents crashes if a field is missing
                    name = h.get('habit_name', 'Unknown')
                    time_val = h.get('timestamp', 'N/A')
                    print(f"[{time_val}] {name}")
            else:
                print(f"⚠️ Unexpected data format: {habits}")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Fetch Error: {e}")

if __name__ == "__main__":
    # Test the pipeline
    log_habit("graham", "Morning Yoga")
    log_habit("graham", "Rust Backend Dev")
    
    time.sleep(0.5)
    get_trends("graham")