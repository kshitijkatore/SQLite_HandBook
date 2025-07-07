import sqlite3
import pandas as pd

DB_FILE = "students.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                grade TEXT,
                city TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_student(name, age, grade, city):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT INTO student (name, age, grade, city) VALUES (?, ?, ?, ?)", (name, age, grade, city))
        conn.commit()

def get_all_students():
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql_query("SELECT * FROM student", conn)

def search_students(grade=None, city=None):
    df = get_all_students()
    if grade and grade != "All":
        df = df[df['grade'] == grade]
    if city:
        df = df[df['city'].str.lower() == city.lower()]
    return df

def update_student(id, name, age, grade, city):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("UPDATE student SET name=?, age=?, grade=?, city=? WHERE id=?", (name, age, grade, city, id))
        conn.commit()

def delete_student_by_id(id):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM student WHERE id=?", (id,))
        conn.commit()
