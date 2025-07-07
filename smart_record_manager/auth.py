import streamlit as st
import sqlite3

DB_FILE = "students.db"

def create_user_table():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)

def register_user(username, password):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

def login_user(username, password):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return cursor.fetchone() is not None

def login_view():
    create_user_table()
    st.title("🔐 Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(login_username, login_password):
            st.session_state.logged_in = True
            st.session_state.user = login_username
            st.success("✅ Logged in successfully.")
        else:
            st.error("❌ Invalid credentials")

    st.markdown("---")
    st.markdown("Don't have an account?")
    reg_user = st.text_input("New Username")
    reg_pass = st.text_input("New Password", type="password")
    if st.button("Register"):
        register_user(reg_user, reg_pass)
        st.success("✅ Registered. Now login.")
