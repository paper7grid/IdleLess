import streamlit as st
import pandas as pd
import altair as alt
import random
st.title("Random Activity Generator")
st.subheader("Step away from your phone. Try something real.")
activities = [
    "Paint a tote bag",
    "Visit a new restaurant in your neighborhood",
    "Take a walk through a park and try to make one new friend",
    "Write a short story, even if it's weird",
    "Bake something you've never tried before",
    "Sketch the view from your window",
    "Organize a mini picnic with someone you haven't talked to in a while",
    "Make a playlist based on your current mood",
    "Go to a local bookstore and pick something at random",
    "Try to do 10 minutes of yoga or stretching",
    "Learn to fold an origami pokeball",
    "Make a mini-documentary about your day using your phone's camera (but no social media!)",
    "Start a journal entry with 'Today felt like...'",
    "Plant something, even if it’s just in a cup of dirt",
    "Recreate a dish from your favorite childhood memory",
    "Write a letter to your future self",
    "Create a tiny scavenger hunt around your room",
    "DIY a piece of jewelry or keychain",
    "Try photographing textures around your home",
    "Build something out of cardboard—literally anything"
    "Rearrange your bedroom furniture",
    "Learn a simple magic trick",
    "Make a collage using old magazines",
    "Build a blanket fort and read inside it",
    "Walk a route you've never taken before",
    "Interview a family member about their childhood",
    "Try painting with coffee or tea",
    "Make a time capsule and bury (or hide) it",
    "Write a poem using only song lyrics",
    "Handwrite a letter to someone you admire",
    "Invent your own board game using stuff around the house",
    "Create a photo series of things that are blue",
    "Create a collage of everything red"
    "Learn to juggle using socks",
    "Try meditating in silence for 15 minutes",
    "Find a random Wikipedia article and draw it",
    "Visit a thrift store and buy something under $5",
    "Make a sculpture using food",
    "Write a scene from a movie, but set in your school or neighborhood",
    "Host a silent dance party with headphones",
    "Paint a rock and leave it somewhere for someone to find",
    "Recreate a moview scene from memory with your friends",
    "Paint or write with you're non-dominant hand",
    "Talk to your neighbours",
    "Declutter you're closet/wardrobe",
    "Create a swing in your backyard",
    "Touch Grass",
    "Make an fruit smoothie",
    "Make Tamales"
]
num = st.slider("How many activity ideas do you want?", 1, 5, 1)
if st.button(":game_die: Give me activities!"):
    selected = random.sample(activities, num)
    for i, activity in enumerate(selected, 1):
        st.markdown(f"**{i}.** {activity}")
else:
    st.caption("Use the slider, then hit the button!")