import sqlite3

DB_NAME = "study.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        plan_date TEXT,
        subjects TEXT,
        study_hours INTEGER,
        study_plan TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_plan(student_name, plan_date, subjects, study_hours, study_plan):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO plans (student_name, plan_date, subjects, study_hours, study_plan)
    VALUES (?, ?, ?, ?, ?)
    """, (student_name, plan_date, subjects, study_hours, study_plan))

    conn.commit()
    conn.close()


def get_plans():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT student_name, plan_date, subjects, study_hours, study_plan
    FROM plans
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows