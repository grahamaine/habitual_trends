import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # ✅ Required for frontend connection
from pydantic import BaseModel
from typing import List, Optional

# Initialize the App
app = FastAPI(title="Habitual Trends API")

# --- ✅ CRITICAL FIX: Add CORS Middleware ---
# This allows your frontend (Reflex/Streamlit) to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change to ["http://localhost:3000"] for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models (Schema) ---
class Habit(BaseModel):
    id: int
    name: str
    streak: int
    last_completed: Optional[str] = None

# --- Mock Database (In-Memory for now) ---
habits_db = [
    {"id": 1, "name": "Drink Water", "streak": 5, "last_completed": "2023-10-27"},
    {"id": 2, "name": "Read Rust Docs", "streak": 12, "last_completed": "2023-10-26"},
]

# --- Routes ---

@app.get("/")
def read_root():
    """Health check and welcome message."""
    return {"message": "Welcome to Habitual Trends API", "status": "active"}

@app.get("/habits", response_model=List[Habit])
def get_habits():
    """Get all current habits."""
    return habits_db

@app.post("/habits")
def create_habit(habit: Habit):
    """Add a new habit."""
    # ✅ FIX: .dict() is deprecated in Pydantic v2, use .model_dump()
    habits_db.append(habit.model_dump())
    return {"message": "Habit created", "data": habit}

@app.get("/health")
def health_check():
    """Fly.io health check endpoint."""
    return {"status": "ok"}

# --- Entry Point ---
if __name__ == "__main__":
    # ✅ FIX: Changed default port to 3005 to match your Frontend config
    port = int(os.environ.get("PORT", 3005))
    
    print(f"🚀 Python Backend running on http://127.0.0.1:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)