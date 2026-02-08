from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Setup - Initialize Base and Engine
Base = declarative_base()
engine = create_engine('sqlite:///your_database.db', echo=True) # echo=True shows the SQL in your console

# 2. Schema - Define your models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

# 3. Execution - Create tables and handle sessions
def init_db():
    # This creates the .db file and the tables
    Base.metadata.create_all(engine)
    
    # Create a session factory
    Session = sessionmaker(bind=engine)
    session = Session()

    # --- Example: Adding a new user ---
    new_user = User(name="Alex")
    session.add(new_user)
    session.commit()
    print("User added successfully!")

if __name__ == "__main__":
    init_db()