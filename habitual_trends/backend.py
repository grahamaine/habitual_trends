from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel
import uvicorn

# --- 1. DATABASE CONFIGURATION ---
DATABASE_URL = "sqlite:///./habits.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database Model
class Habit(Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    streak = Column(Integer, default=0)

# Create the database and tables
Base.metadata.create_all(bind=engine)

# --- 2. API SETUP ---
app = FastAPI(title="Habitual Trends Backend")

# CORS Middleware (Allows Reflex to talk to this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic schema for creating habits
class HabitCreate(BaseModel):
    name: str

# --- 3. ROUTES ---

@app.get("/api/habits")
async def get_habits():
    db = SessionLocal()
    try:
        return db.query(Habit).all()
    finally:
        db.close()

@app.post("/api/habits")
async def add_habit(habit_data: HabitCreate):
    db = SessionLocal()
    try:
        new_habit = Habit(name=habit_data.name, streak=0)
        db.add(new_habit)
        db.commit()
        db.refresh(new_habit)
        return new_habit
    finally:
        db.close()

@app.put("/api/habits/{habit_id}/increment")
async def increment_streak(habit_id: int):
    db = SessionLocal()
    try:
        habit = db.query(Habit).filter(Habit.id == habit_id).first()
        if habit:
            habit.streak += 1
            db.commit()
            db.refresh(habit)
            return habit
        return {"error": "Habit not found"}, 404
    finally:
        db.close()

@app.delete("/api/habits/{habit_id}")
async def delete_habit(habit_id: int):
    db = SessionLocal()
    try:
        habit = db.query(Habit).filter(Habit.id == habit_id).first()
        if habit:
            db.delete(habit)
            db.commit()
            return {"message": "Deleted successfully"}
        return {"error": "Habit not found"}, 404
    finally:
        db.close()

# --- 4. EXECUTION ---
if __name__ == "__main__":
    # Runs the server on port 3005
    uvicorn.run(app, host="127.0.0.1", port=3005)