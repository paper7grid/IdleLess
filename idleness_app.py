# IdleLess: Traffic Idle Time Visualization Streamlit App (Simplified for SF & Fremont)

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="IdleLess Dashboard", page_icon="🚦")
st.title("🚦 IdleLess: Reducing Urban Idle Time")

st.write("""
This app focuses on traffic idle patterns in **San Francisco (SF)** and **Fremont**, visualizing the hours of the day when idling peaks. This helps drivers make better choices and highlights unnecessary fuel waste.
""")

# --- Simplified Static Data ---
data = {
    "city": ["SF"] * 6 + ["Fremont"] * 6,
    "hour": ["6:00 AM", "9:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "9:00 PM"] * 2,
    "idle_time_estimate": [12, 25, 15, 20, 30, 10, 8, 18, 10, 14, 22, 6]
}
df = pd.DataFrame(data)

# --- Select City ---
cities = df["city"].unique().tolist()
selected_city = st.radio("Choose a city:", cities, horizontal=True)
filtered_df = df[df["city"] == selected_city]

# --- Idle Time Chart ---
st.subheader(f"Estimated Idle Time by Hour in {selected_city}")
chart = (
    alt.Chart(filtered_df)
    .mark_bar(color="#ff6347")
    .encode(
        x=alt.X("hour", sort=None, title="Hour of Day"),
        y=alt.Y("idle_time_estimate", title="Idle Time (minutes)"),
        tooltip=["hour", "idle_time_estimate"]
    )
    .properties(height=400)
)
st.altair_chart(chart, use_container_width=True)

# --- Summary ---
max_idle = filtered_df["idle_time_estimate"].max()
worst_hour = filtered_df.loc[filtered_df["idle_time_estimate"].idxmax(), "hour"]

st.markdown(f"⏱️ **Worst Idle Time** in {selected_city} is at **{worst_hour}**, with about **{max_idle} minutes** wasted.")

# --- Notes ---
st.markdown("""
---
### 🚗 Why This Project?
- Even short idle periods add up across a city.
- Knowing peak idling times helps reduce traffic pollution.
- Local focus on **SF** and **Fremont** keeps it realistic and manageable.

*Built by a student using Streamlit, Pandas, and Altair.*
""")
