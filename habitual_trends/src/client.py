import requests

# This must match the addr in your Rust main.rs
BASE_URL = "http://127.0.0.1:3000" 

def get_trends(username):
    url = f"{BASE_URL}/api/trends/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            habits = response.json()
            if isinstance(habits, list):
                print(f"\n--- Trends for {username} ---")
                for h in habits:
                    # 'timestamp' and 'habit_name' match your Rust Habit struct
                    print(f"[{h.get('timestamp', 'N/A')}] {h.get('habit_name', 'Unknown')}")
            else:
                print(f"Unexpected data format: {habits}")
        else:
            print(f"❌ Server returned error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

# Example of how to actually call the function
if __name__ == "__main__":
    user = input("Enter username to see trends: ")
    get_trends(user)