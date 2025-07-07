import streamlit as st
from db import init_db
from views import add_view, view_records, search_view, stats_view, export_view, update_delete_view, graph_view
from auth import login_view

st.set_page_config(page_title="Smart Record Manager", layout="centered")
st.title("🎓 Smart Record Manager (Web App)")

# Login check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_view()
    st.stop()

# Init DB
init_db()

# Menu
menu = st.sidebar.radio("Menu", ["Add Student", "View Students", "Search", "Update/Delete", "Statistics", "Visualize", "Export"])

if menu == "Add Student":
    add_view()
elif menu == "View Students":
    view_records()
elif menu == "Search":
    search_view()
elif menu == "Update/Delete":
    update_delete_view()
elif menu == "Statistics":
    stats_view()
elif menu == "Visualize":
    graph_view()
elif menu == "Export":
    export_view()
