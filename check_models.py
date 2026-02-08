from google import genai

# Use your working key
client = genai.Client(api_key="AIzaSyA-kVfYYHIg_oPJlD8IromotoPMPpQQmVU")

print("?? Fetching available models...")
try:
    # List all models
    for m in client.models.list():
        if "generateContent" in m.supported_generation_methods:
            print(f"? Found: {m.name}")
except Exception as e:
    print(f"? Error: {e}")
