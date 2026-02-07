import streamlit as st
import requests
import pandas as pd
import time

# ==========================================
# 1. CONFIGURATION & CONSTANTS
# ==========================================
API_URL = "http://127.0.0.1:8080"  # Make sure this matches your FastAPI port (usually 8000 or 8080)
USE_MOCK_DATA = True  # Set to False when you are ready to connect to the real Backend

st.set_page_config(
    page_title="Habitual Trends",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a cleaner look
st.markdown("""
    <style>
        .block-container {padding-top: 1.5rem;}
        div[data-testid="stMetricValue"] {font-size: 26px; color: #4F46E5;}
        .stButton button {border-radius: 8px; font-weight: 600;}
        div[data-testid="stToast"] {width: fit-content;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. STATE MANAGEMENT
# ==========================================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""
if "page" not in st.session_state:
    st.session_state["page"] = "Dashboard"

# ==========================================
# 3. HELPER FUNCTIONS
# ==========================================
def api_request(method, endpoint, data=None):
    """
    Handles API requests.
    If USE_MOCK_DATA is True, it simulates a successful response.
    """
    if USE_MOCK_DATA:
        time.sleep(0.5) # Simulate network delay
        # Mock Response Object
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data
            def json(self): return self.json_data
            @property
            def text(self): return str(self.json_data)
        
        if endpoint == "/login":
            # Simulate successful login for any email
            return MockResponse(200, {"message": "Login successful"})
        return MockResponse(200, {"message": "Success"})

    # --- Real Backend Logic ---
    try:
        url = f"{API_URL}{endpoint}"
        if method == "POST":
            return requests.post(url, json=data, timeout=5)
        return requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError:
        st.toast("Backend offline: Is 'main.py' running?", icon="⚠️")
        return None
    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return None

def logout():
    st.session_state["logged_in"] = False
    st.session_state["user_email"] = ""
    st.session_state["page"] = "Dashboard"
    st.rerun()

# =