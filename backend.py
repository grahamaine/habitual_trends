from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel
import uvicorn

# 1. DATABASE SETUP
Base = declarative_base()
engine = create_engine('sqlite:///habits.db', echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

class Habit(Base):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    streak = Column(Integer, default=0)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)

# 2. FASTAPI APP
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class HabitCreate(BaseModel):
    name: str

# 3. ROUTES
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
        new_habit = Habit(name=habit_data.name)
        db.add(new_habit)
        db.commit()
        db.refresh(new_habit)
        return new_habit
    finally:
        db.close()

# --- NEW INCREMENT ROUTE ---
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
        # Raise an actual HTTP 404 error
        raise HTTPException(status_code=404, detail="Habit not found")
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
            return {"message": "Deleted"}
        raise HTTPException(status_code=404, detail="Habit not found")
    finally:
        db.close()

# 4. START SERVER
if __name__ == "__main__":
    # Note: Running on 3005 to avoid your previous port 3000 conflict
    uvicorn.run(app, host="127.0.0.1", port=3005)