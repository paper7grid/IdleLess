import streamlit as st
import random
from datetime import date
st.set_page_config(page_title="Random Activity Generator", layout="centered")
# Toggle for Theme
is_dark = st.toggle("Dark Mode")
# CSS for Both Themes
if not is_dark:
    st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e8ecf5, #f5e8f5);
        font-family: 'Segoe UI', sans-serif;
        color: #111 !important;
    }
    html, body, p, div, span, h1, h2, h3, h4, h5, h6, label {
        color: #111 !important;
    }
    .title {
        font-size: 3em;
        text-align: center;
        margin-top: 0.5em;
        color: #111 !important;
    }
    .subtitle {
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 2em;
        color: #222 !important;
    }
    .activity-box {
        background-color: #fff;
        padding: 1em;
        margin: 0.5em 0;
        border-left: 6px solid #a98cd9;
        border-radius: 10px;
        font-size: 1.2em;
        color: #111 !important;
    }
    /* --- BUTTON FIXES --- */
    button {
        background-color: #ffffff !important;
        color: #111 !important;
        font-weight: bold !important;
        border: 2px solid #a98cd9 !important;
        border-radius: 8px !important;
        padding: 0.75em 1.5em !important;
        font-size: 1.1em !important;
    }
    button:hover {
        background-color: #f2f2f2 !important;
        border-color: #9e80cc !important;
    }
    /* --- SLIDER + TEXT FIXES --- */
    .stSlider > div > div > div {
        background: #a98cd9 !important;
    }
    .stSlider label, .stSlider span,
    .st-dh, .st-de, .st-b1 {
        color: #222 !important;
    }
</style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #1e1e2f, #2c2c3c);
                font-family: 'Segoe UI', sans-serif;
                color: white !important;
            }
            html, body, p, div, span, h1, h2, h3, h4, h5, h6, label {
                color: white !important;
            }
            .title {
                font-size: 3em;
                text-align: center;
                margin-top: 0.5em;
                color: white !important;
            }
            .subtitle {
                font-size: 1.5em;
                text-align: center;
                margin-bottom: 2em;
                color: #ddd !important;
            }
            .activity-box {
                background-color: #2f2f44;
                padding: 1em;
                margin: 0.5em 0;
                border-left: 6px solid #b495d9;
                border-radius: 10px;
                font-size: 1.2em;
                color: white !important;
            }
            button[kind="primary"] {
                background-color: white !important;
                color: black !important;
                font-weight: bold;
                border: 2px solid #b495d9 !important;
                border-radius: 8px !important;
                padding: 0.75em 1.5em !important;
                font-size: 1.1em !important;
            }
            button[kind="primary"]:hover {
                background-color: #eeeeee !important;
                border-color: #c2a8f2 !important;
            }
            .stSlider > div > div > div {
                background: #b495d9 !important;
            }
            .stSlider label, .stSlider span {
                font-weight: normal !important;
                color: #ccc !important;
            }
        </style>
    """, unsafe_allow_html=True)
# Title + Subtitlet
st.markdown('<div class="title">:no_mobile_phones:Random Activity Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Step away from your screen. Try something real</div>', unsafe_allow_html=True)
# Activities List
activities = [
    "Paint a tote bag", "Visit a new restaurant in your neighborhood",
    "Take a walk through a park and try to make one new friend",
    "Write a short story, even if it's weird", "Bake something you've never tried before",
    "Sketch the view from your window", "Organize a mini picnic with someone you haven't talked to in a while",
    "Make a playlist based on your current mood", "Go to a local bookstore and pick something at random",
    "Try to do 10 minutes of yoga or stretching", "Learn to fold an origami pokeball",
    "Make a mini-documentary about your day using your phone's camera (but no social media!)",
    "Start a journal entry with 'Today felt like...'", "Plant something, even if it's just in a cup of dirt",
    "Recreate a dish from your favorite childhood memory", "Write a letter to your future self",
    "Create a tiny scavenger hunt around your room", "DIY a piece of jewelry or keychain",
    "Try photographing textures around your home", "Build something out of cardboard—literally anything",
    "Rearrange your bedroom furniture", "Learn a simple magic trick",
    "Make a collage using old magazines", "Build a blanket fort and read inside it",
    "Walk a route you've never taken before", "Interview a family member about their childhood",
    "Try painting with coffee or tea", "Make a time capsule and bury (or hide) it",
    "Write a poem using only song lyrics", "Handwrite a letter to someone you admire",
    "Invent your own board game using stuff around the house",
    "Create a photo series of things that are blue", "Create a collage of everything red",
    "Learn to juggle using socks", "Try meditating in silence for 15 minutes",
    "Find a random Wikipedia article and draw it", "Visit a thrift store and buy something under $5",
    "Make a sculpture using food", "Write a scene from a movie, but set in your school or neighborhood",
    "Host a silent dance party with headphones", "Paint a rock and leave it somewhere for someone to find",
    "Recreate a movie scene from memory with your friends", "Paint or write with your non-dominant hand",
    "Talk to your neighbors", "Declutter your closet/wardrobe",
    "Create a swing in your backyard", "Touch grass (literally)",
    "Make a fruit smoothie", "Make tamales"
]
num = st.slider("How many activity ideas do you want?", 1, 10, 1)
if "selected" not in st.session_state:
    st.session_state.selected = []
def pick_activities():
    st.session_state.selected = random.sample(activities, num)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Give me activities!"):
        pick_activities()
    if st.button("Spin Again"):
        pick_activities()
    if st.session_state.selected:
        for i, activity in enumerate(st.session_state.selected, 1):
            st.markdown(f'<div class="activity-box">{i}. {activity}</div>', unsafe_allow_html=True)
            st.checkbox("I did this!", key=f"done_{i}")
    else:
        st.caption("Use the slider above, then hit the button!")
# Daily challenge
daily_rng = random.Random(str(date.today()))
daily_activity = daily_rng.choice(activities)
st.markdown(f"**Today's Challenge:** *{daily_activity}*")
# Mood-based suggestion
if "mood_suggestion" not in st.session_state:
    st.session_state.mood_suggestion = ""
mood = st.radio("What's your vibe right now?", ["Chill", "Creative", "Active", "Social", "Surprise me!"])
if st.button("Suggest one activity for this mood"):
    mood_rng = random.Random()
    st.session_state.mood_suggestion = mood_rng.choice(activities)
if st.session_state.mood_suggestion:
    st.markdown(f"Try this: **{st.session_state.mood_suggestion}**")
# User idea submission
user_idea = st.text_input("Got your own cool idea? Add it here!")
if st.button("Submit my idea"):
    st.success("Nice! Your idea's been noted (in spirit).")
# Footer
st.markdown("""
<hr style="margin-top: 3em; margin-bottom: 1em;">
<div style="text-align: center; font-size: 1.1em; color: inherit;">
    Found a favorite activity? Screenshot it and do it <i>right now</i>.<br>
    Or... hit the button again and keep exploring.
    <br><br>
    Small moments > screen time.
</div>
""", unsafe_allow_html=True)
st.markdown("""
<hr style="margin-top: 3em; margin-bottom: 1em;">
<div style="text-align: center; font-size: 1.1em; color: inherit;">
    <i>Still feeling bored? Check out this <a href="https://www.healthline.com/health/boredom#causes" target="_blank" style="color: inherit; text-decoration: underline;">link</a>.</i>
</div>
""", unsafe_allow_html=True)