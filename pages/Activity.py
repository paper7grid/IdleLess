import streamlit as st
import pandas as pd
import altair as alt
import random
activities = [
    "🎨 Paint or draw something creative!",
    "📚 Read a book or magazine.",
    "🚶‍♀️ Take a walk outside.",
    "🧁 Bake or cook a new recipe.",
    "📝 Write a journal or letter.",
    "🎵 Listen to music mindfully.",
    "🧩 Solve a puzzle or play a board game.",
    "🌿 Try indoor gardening or plant care.",
]

st.header("Need a break from screens?")
if "activity" not in st.session_state:
    st.session_state.activity = random.choice(activities)

if st.button("Give me a new idea!"):
    st.session_state.activity = random.choice(activities)

st.success(st.session_state.activity)

st.markdown("---")