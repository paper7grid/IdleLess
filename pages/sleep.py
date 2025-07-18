import streamlit as st
import pandas as pd
import altair as alt
import random

st.set_page_config(page_title="Screen Time & Mental Health", page_icon="📱")

st.title("Screen Time & Mental Health: Explore Your Data")

st.write("""
Welcome! Enter your daily screen time and sleep hours below to see how they compare to general trends in stress and mood.
""")

# --- User inputs ---
screen_time_input = st.number_input(
    "Enter your total daily screen time (hours):", min_value=0.0, max_value=24.0, value=3.0, step=0.1
)

sleep_hours_input = st.number_input(
    "Enter your average sleep per night (hours):", min_value=0.0, max_value=24.0, value=7.0, step=0.1
)

# --- Quick insight based on user input ---
def screen_time_stress_note(hours):
    if hours < 4:
        return "Your screen time is relatively low — generally linked with lower stress."
    elif hours < 6:
        return "Moderate screen time — some risk of increased stress."
    else:
        return "High screen time! This often correlates with higher stress levels."

def sleep_mood_note(hours):
    if hours < 6:
        return "Less than 6 hours of sleep may lower mood scores."
    elif hours <= 8:
        return "Good sleep range! Usually linked with better mood."
    else:
        return "More than 8 hours of sleep can sometimes reduce mood scores."

st.markdown("### Your personalized notes:")
st.write(f"- Screen time note: {screen_time_stress_note(screen_time_input)}")
st.write(f"- Sleep note: {sleep_mood_note(sleep_hours_input)}")

st.markdown("---")
# Fun offline activity suggestions
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


# --- Load and prepare dataset ---
df = pd.read_csv("digital_habits_vs_mental_health.csv").dropna(subset=["screen_time_hours", "stress_level", "sleep_hours", "mood_score"])

screen_bins = [0, 2, 4, 6, 8, 10, 24]
screen_labels = ["0-2", "2-4", "4-6", "6-8", "8-10", "10+"]
df['screen_bin'] = pd.cut(df['screen_time_hours'], bins=screen_bins, labels=screen_labels)

sleep_bins = [0, 4, 6, 8, 10, 12]
sleep_labels = ["0-4", "4-6", "6-8", "8-10", "10+"]
df['sleep_bin'] = pd.cut(df['sleep_hours'], bins=sleep_bins, labels=sleep_labels)

stress_stats = df.groupby('screen_bin')['stress_level'].agg(['mean', 'count', 'std']).reset_index()
stress_stats['stderr'] = stress_stats['std'] / stress_stats['count']**0.5
stress_stats['lower'] = stress_stats['mean'] - stress_stats['stderr']
stress_stats['upper'] = stress_stats['mean'] + stress_stats['stderr']

mood_stats = df.groupby('sleep_bin')['mood_score'].agg(['mean', 'count', 'std']).reset_index()
mood_stats['stderr'] = mood_stats['std'] / mood_stats['count']**0.5
mood_stats['lower'] = mood_stats['mean'] - mood_stats['stderr']
mood_stats['upper'] = mood_stats['mean'] + mood_stats['stderr']

# --- Graphs ---

st.subheader("Average Stress Level by Screen Time")

stress_line = alt.Chart(stress_stats).mark_line(point=True, color='red').encode(
    x=alt.X('screen_bin', title='Screen Time (hours)'),
    y=alt.Y('mean', title='Average Stress Level'),
    tooltip=['screen_bin', alt.Tooltip('mean', format=".2f"), 'count']
)

stress_error = alt.Chart(stress_stats).mark_errorbar().encode(
    x='screen_bin',
    y='lower',
    y2='upper'
)

st.altair_chart(stress_line + stress_error, use_container_width=True)

st.write("More screen time generally means higher stress, especially after 6 hours per day.")

st.subheader("Average Mood Score by Sleep Hours")

mood_line = alt.Chart(mood_stats).mark_line(point=True, color='green').encode(
    x=alt.X('sleep_bin', title='Sleep Hours'),
    y=alt.Y('mean', title='Average Mood Score'),
    tooltip=['sleep_bin', alt.Tooltip('mean', format=".2f"), 'count']
)

mood_error = alt.Chart(mood_stats).mark_errorbar(color='green').encode(
    x='sleep_bin',
    y='lower',
    y2='upper'
)

st.altair_chart(mood_line + mood_error, use_container_width=True)

st.write("Mood scores tend to be higher for people who sleep between 6 and 8 hours.")

st.markdown("---")

# --- Conclusion ---
st.header("Final Thoughts")

st.write("""
Based on data from many people:  
- Limiting screen time to under 6 hours can help reduce stress levels.  
- Getting between 6 and 8 hours of sleep is linked with better mood and wellbeing.  

Try balancing your digital habits and sleep schedule to support your mental health!  
""")
