import sqlite3


def create_database():
    conn = sqlite3.connect("tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
     id INTEGER PRIMARY KEY,
     name TEXT,
     age INTEGER,
     weight REAL,
     height REAL
     goal_weight REAL
    )
""")

    cursor.execute("""
    CREATE Table IF NOT EXISTS meals (
     id INTEGER PRIMARY KEY,
     meal_name TEXT,
     calories REAL,
     carbs REAL,
     protein REAL,
     fat REAL,
     date TEXT,
     time TEXT
)
""")

    cursor.execute("""
    CREATE Table IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY,
    exercise_name TEXT,
    exercise_duration INTEGER,
    calories_burned REAL,
    date TEXT
)
""")
    conn.commit()
    conn.close()
    print("Database created successfully")

create_database()