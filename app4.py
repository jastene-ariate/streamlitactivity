import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# ✅ MySQL connection string (no password)
DATABASE_URL = "mysql+pymysql://root@localhost:3306/streamlitariate"
engine = create_engine(DATABASE_URL)

# Session state for login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "current_user" not in st.session_state:
    st.session_state.current_user = ""

# ---------------- Sidebar Registration ----------------
st.sidebar.header("🔐 Register New Account")
with st.sidebar.form("register_form"):
    new_name = st.text_input("Full Name")
    new_password = st.text_input("Password", type="password")
    register_btn = st.form_submit_button("Register")

    if register_btn:
        if new_name and new_password:
            try:
                with engine.begin() as conn:
                    # Insert the new user into the users table with name and password
                    conn.execute(
                        text("INSERT INTO users (name, password) VALUES (:n, :p)"),
                        {"n": new_name, "p": new_password}
                    )
                st.sidebar.success("✅ Registered successfully!")
            except Exception as e:
                st.sidebar.error(f"❌ Registration failed: {e}")
        else:
            st.sidebar.warning("Please complete all fields.")

# ---------------- Login Section ----------------
if not st.session_state.authenticated:
    st.title("🔒 User Login")
    with st.form("login_form"):
        username = st.text_input("Name")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            with engine.connect() as conn:
                # Check if the entered name and password exist in the users table
                result = conn.execute(
                    text("SELECT * FROM users WHERE name = :n AND password = :p"),
                    {"n": username, "p": password}
                ).fetchone()

            if result:
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.success(f"✅ Welcome, {username}!")
            else:
                st.error("❌ Invalid credentials.")

# ---------------- Main App ----------------
if st.session_state.authenticated:
    st.title("📋 User Data Manager")
    st.caption(f"Logged in as: `{st.session_state.current_user}`")

    # 🔍 Filter Users
    st.subheader("🔍 Search Users")
    filter_name = st.text_input("Filter by name")
    query = "SELECT * FROM users"
    params = {}

    if filter_name:
        query += " WHERE name LIKE :name"
        params["name"] = f"%{filter_name}%"

    df = pd.read_sql(text(query), engine, params=params)
    st.dataframe(df)

    # ➕ Insert New User
    st.subheader("➕ Add New User")
    with st.form("add_user_form"):
        name = st.text_input("Name")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Insert")

        if submit:
            if name and password:
                with engine.begin() as conn:
                    conn.execute(
                        text("INSERT INTO users (name, password) VALUES (:name, :password)"),
                        {"name": name, "password": password}
                    )
                st.success("✅ User added!")
            else:
                st.warning("Name and Password are required.")
