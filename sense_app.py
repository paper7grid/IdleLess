import streamlit as st

st.set_page_config(page_title="ScrollScope", page_icon="📱", layout="centered")

st.title("📱 ScrollScope")
st.subheader("Understand Your Digital Habits and Mental Health")

st.write("Welcome to **ScrollScope** – a project that helps you explore how your screen time and sleep habits connect to stress and mood.")

# --- Sidebar navigation ---
st.sidebar.title("📂 Navigation")
st.sidebar.markdown("Choose a page:")

st.sidebar.page_link("pages/Mental_Health.py", label="Mental Health Insights")
st.sidebar.page_link("pages/Activity.py", label="Activity Generator")

st.markdown("---")
st.markdown("Use the **sidebar** to navigate!")
