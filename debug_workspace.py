import configparser
import os
import requests

# 1. Read the API Key from your local config
config_path = os.path.expanduser("~/.opik.config")
config = configparser.ConfigParser()
config.read(config_path)

if 'opik' not in config or 'api_key' not in config['opik']:
    print("? Error: Could not find API Key in .opik.config")
    exit()

api_key = config['opik']['api_key']
print(f"?? Found API Key: {api_key[:6]}...")

# 2. Query the Opik API for available workspaces
url = "https://www.comet.com/opik/api/v1/workspaces"
headers = {
    "Comet-Workspace": "default", 
    "Authorization": api_key,
    "Content-Type": "application/json"
}

try:
    print(f"?? Querying: {url}...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("\n? SUCCESS! Here are your valid workspaces:")
        print("------------------------------------------")
        if 'content' in data:
            for ws in data['content']:
                print(f"?? Name: {ws.get('name')}")
        else:
            print(data)
        print("------------------------------------------")
    else:
        print(f"\n? Server Error {response.status_code}:")
        print(response.text)
        
except Exception as e:
    print(f"\n? Connection Error: {e}")
