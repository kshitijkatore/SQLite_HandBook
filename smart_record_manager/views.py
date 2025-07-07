import streamlit as st
from db import add_student, get_all_students, search_students, update_student, delete_student_by_id
import matplotlib.pyplot as plt
import plotly.express as px

def add_view():
    st.subheader("➕ Add New Student")
    with st.form("add_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, step=1)
        grade = st.selectbox("Grade", ["A", "B", "C"])
        city = st.text_input("City")
        submit = st.form_submit_button("Add")
        if submit:
            add_student(name, age, grade, city)
            st.success(f"✅ Student '{name}' added successfully!")

def view_records():
    st.subheader("📋 All Student Records")
    df = get_all_students()
    st.dataframe(df)

def search_view():
    st.subheader("🔍 Search Students")
    grade = st.selectbox("Filter by Grade", ["All", "A", "B", "C"])
    city = st.text_input("Filter by City")
    df = search_students(grade, city)
    st.dataframe(df)

def stats_view():
    st.subheader("📈 Student Statistics")
    df = get_all_students()
    if df.empty:
        st.warning("No data available.")
        return
    st.metric("👥 Total Students", df.shape[0])
    st.metric("📊 Average Age", round(df['age'].mean(), 2))
    st.metric("🎯 Grade A Count", df[df['grade'] == 'A'].shape[0])

def export_view():
    st.subheader("📄 Export Data to CSV")
    df = get_all_students()
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv, "students.csv", "text/csv")

def update_delete_view():
    st.subheader("✏️ Update / 🗑️ Delete Student")
    df = get_all_students()
    if df.empty:
        st.warning("No students found.")
        return
    selected = st.selectbox("Select a student by ID", df['id'])
    student = df[df['id'] == selected].iloc[0]
    name = st.text_input("Name", value=student['name'])
    age = st.number_input("Age", value=int(student['age']))
    grade = st.selectbox("Grade", ["A", "B", "C"], index=["A", "B", "C"].index(student['grade']))
    city = st.text_input("City", value=student['city'])
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Update"):
            update_student(selected, name, age, grade, city)
            st.success("Student updated.")
    with col2:
        if st.button("🗑️ Delete"):
            delete_student_by_id(selected)
            st.success("Student deleted.")

def graph_view():
    st.subheader("📊 Visualize Student Data")
    df = get_all_students()
    if df.empty:
        st.warning("No data to visualize.")
        return
    st.write("### Grade Distribution (Pie Chart)")
    fig1 = px.pie(df, names='grade', title='Grade Breakdown')
    st.plotly_chart(fig1)
    st.write("### Age Distribution (Histogram)")
    fig2, ax = plt.subplots()
    ax.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
    ax.set_title("Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")
    st.pyplot(fig2)
