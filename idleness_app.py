# IdleLess: Traffic Idle Time Visualization Streamlit App

import streamlit as st
import pandas as pd
import altair as alt
import requests
from datetime import datetime

st.set_page_config(page_title="IdleLess Dashboard", page_icon="🚦")
st.title("🚦 IdleLess: Reducing Urban Idle Time")

st.write("""
This app analyzes traffic patterns and idle-heavy times using publicly available datasets to help reduce unnecessary emissions and time lost in traffic. Our goal is to visualize when and where cars tend to idle the most and provide actionable insights.
""")

# --- LOAD DATA ---
@st.cache_data
def load_sample_data():
    # Replace with real API or dataset
    url = "https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv"
    df = pd.read_csv(url)
    df = df.rename(columns={"cnt": "idle_time_estimate"})
    df = df.head(100)  # Simulated small dataset
    df["city"] = df["airport"].apply(lambda x: x[:3])
    df["hour"] = pd.Series([i % 24 for i in range(len(df))])
    return df

traffic_df = load_sample_data()

# --- USER FILTERS ---
cities = traffic_df["city"].unique().tolist()
selected_city = st.selectbox("Select a city code:", cities)

filtered_df = traffic_df[traffic_df["city"] == selected_city]

# --- CHART: IDLE TIME BY HOUR ---
st.subheader(f"Idle Time Pattern for {selected_city}")
chart = (
    alt.Chart(filtered_df)
    .mark_bar(color="orangered")
    .encode(
        x=alt.X("hour:O", title="Hour of Day"),
        y=alt.Y("idle_time_estimate:Q", title="Estimated Idle Time (minutes)"),
        tooltip=["hour", "idle_time_estimate"]
    )
    .properties(height=400)
)
st.altair_chart(chart, use_container_width=True)

# --- TEXT INSIGHT ---
max_idle = filtered_df["idle_time_estimate"].max()
worst_hour = filtered_df.loc[filtered_df["idle_time_estimate"].idxmax(), "hour"]

st.markdown(f"⏱️ **Peak Idle Hour**: Around **{worst_hour}:00**, with up to **{int(max_idle)} minutes** of estimated idle time.")

# --- ADDITIONAL CONTEXT ---
st.markdown("""
### Why This Matters:
- Car idling contributes to **greenhouse gas emissions** and **fuel waste**.
- Understanding idle patterns helps city planners improve traffic signal timing.
- Drivers can save money and time by avoiding peak idle periods.

### Data Notes:
- Idle time estimates are simulated from airport traffic data for demo purposes.
- Real implementation would use APIs like **OpenTraffic**, **Bay Area 511**, or **EPA emission datasets**.

---
*Built with Streamlit, Pandas, Altair. Inspired by real-world inefficiencies in city traffic systems.*
""")
