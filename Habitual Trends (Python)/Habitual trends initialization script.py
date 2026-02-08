import sqlite3
from datetime import datetime

#Connect to (or create) the database conn = sqlite3.connect('health_app.db') cursor = conn.cursor()
def init_db():
    #1. User's Table 
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, created-at TIMMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')
    #2. Habits Table (The definitions)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT NOT NULL,
    desciption TEXT,
    frequency TEXT DEFAULT 'daily', --daily, weekly target value INTEGER DEFAULT 1, -- e.g., 2000 (ml of water)
    unit TEXT, --e.g., "ml", "mins", "boolean"
    FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''')
    #3. Habits Logs (The daily execution)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS habit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER,
    value_logged REAL, --HOw much did they do?
    notes TEXT,
    logged_at TIMESTAMP DEFAULT
    CURRENT_TIMESTAMP,
    date_logged DATE NOT NULL, --YYYY-MM-DD for
    easy grouping
    FOREIGN KEY(habit_id) REFERENCES habits(id)
    )
    ''')
    conn.commit()
    print("Database initialized succesfully.")
    if_name__=="__main__":
        init_db()

import sqlite3
        from datetime import datetime, timedelta

        def get_db_connection():
            return sqlite3.connect('health_app.db')

            #---Core Scripting Fnuctions---
            def log_habit(habit_id, value, notes=""):
                """Script to log a habit entry for today."""
                conn=get_db_connnection()
                cur=conn.cursor()
                today = datetime.now().strftime('%Y-%m-%d')

                cur.exectue('''
                INSERT INTO habit_logs (habit_id, value_logged, notes, dates logged)
                VALUES (?, ?, ?, ?)
                ''', (habit_id, value, notes, today))

                conn.commit()
                conn.close()
                print("Logged habit {habit_id} for {today}" )

                def calculate_streak(habit_id):
                    """
                    ALGORITHIM: Calculate the current consecutive day streak.
                    This is a perfect place to script complex logic (e.g., allow 1 miss).
                    """

                    conn = get_db_connection()
                    cur = conn.cursor()

# Get all distint dates logs for this habit, ordered latest first
cur.execute('''
SELECT DISTINCT date_logged
FROM habit_logs
WHERE habit_id = ?
ORDER BY date_logged DESC
''', (habit_id))

dates = [row[0] for row in cur.fetchall()]
conn.close()

if not dates:
    return 0

streak = 0
#Check today
today_str = datetime.now().strftime('%Y-%m-%d')
yesterday_str = (datetime.now() -
timedelta(days=1)).strftime('%Y-%m-%d')

#If the latest log is not today or yesterday, streak is borken immediately
if dates[0] !=today_str and dates[0] !=yesterday_str: return 0

#Iterate backwards to count consecutive days
current_check = datetime.strptime(dates[0], '%Y-%m-%d')

for i, date_str in enumerate(dates):
    log_date = datetime.strptime(dates[0], '%y-%m-%d')

# Calculate difference between this log and the checking date
diff = (current_check - log_date).days

if i ==0: #first itema matches automatically 
streak +=1
elif diff ==1: #Consecutive day found
streak +=1
current_check = log_date #Move check pointer back 
else:
    break #Gap found, streak ends

return streak

def analyse_weekly_trend(habit_id):
    """Returns the total value logged over the last 7 days."""
    conn = get_db_connection()
    cur = conn.cursor()

    seven_days_ago = (datetime.now() -
    timedelta(days=7)).strftime('%Y-%m-%d')

cur.execute('''
SELECT SUM(valu_logged)
FROM habit_logs
WHERE habit_id = ? AND date_logged>=?
''', (habit_id, seven_days_ago))

result = cur.fetchone()[0]
conn.close()
return result if result else 0

# ---Test Your Script---
if__name__== "__main__":
    #Example usage:
    #1. Manually insert a habit if DB is empty (Scripting setup)
    #2. Run log_habit(1, 100)
    #3. Print(calculate_streaK(1))
    print("Analytics module ready.")

import sys 
from models import init_db
from Analytics import log_habit, calculate_streak, analyze_weekly_trend

def main():
    print("---Habitual Trends Scripting Interface ---")
    print("1. Intialize DB")
    print("2. Log Habit")
    print("3. Check Streak")
    print("4. Check Weekly Trend")

    choice = input("Select operation (1-4):")

    if choice =='1':
        init_db()
        elif choice =='2':
            h_id = input("Habit ID:")
            val = input("Value:")
            log_habit(h_id,val)
            elif choice =='3':
                h_id = input ("Habit ID:")
                print(f"Current Streak:{calculate_streak(h_id)}days")
                elif choice =='4':
                    h_id = input("Habit ID:")
                    print(f"Last 7 Days Total:
                    {analyze_weekly_trend(h_id)}")
                    else:
                        print("Invalid choice")

    if__name__=="__main__":
        main()
        