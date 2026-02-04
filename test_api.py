import requests

def test_connection():
    # We added your name to the end of the URL to match the Rust dynamic route
    url = "http://127.0.0.1:3000/api/trends/graham" 
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Rust backend.")

if __name__ == "__main__":
    test_connection()