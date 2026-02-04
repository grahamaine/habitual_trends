import requests
import sys

# Configuration
BASE_URL = "http://127.0.0.1:3005"
USERNAME = "graham"  # You can change this or add an input for it

def log_habit(habit_name):
    """Sends a habit to the Rust/SQLite backend."""
    url = f"{BASE_URL}/api/habits"
    payload = {"user": USERNAME, "habit_name": habit_name}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            print(f"✅ Saved: '{habit_name}'")
            # Immediately fetch the new lifetime count for this habit
            get_count(habit_name)
        else:
            print(f"❌ Failed to save. Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection Error: Ensure your Rust server is running on 3005.")

def get_count(habit_name):
    """Fetches how many times you've done this specific habit."""
    url = f"{BASE_URL}/api/count/{USERNAME}/{habit_name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            count = data.get("total_count", 0)
            print(f"📊 Lifetime total for {habit_name}: {count}")
    except:
        pass # Silently fail if count fetch fails

def main():
    print(f"--- Habitual Trends Input (User: {USERNAME}) ---")
    print("Type your habit and press Enter. (Type 'exit' to quit)")
    
    while True:
        try:
            user_input = input("\nWhat did you complete? > ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
                
            if user_input:
                log_habit(user_input)
            else:
                print("Please enter a habit name.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()