import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="TUMO Workshop Projects", layout="wide")

st.title("TUMO Workshop — 8 Mini Projects")
st.markdown("As it is a live demo, you can interact with these applications right here")
st.divider()

# (folder name, display title, iframe height in px)
PROJECTS = [
    ("project1 - Digital Clock",            "Session 1 — Digital Clock",            600),
    ("project2 - Age Calculator",           "Session 2 — Age Calculator",           680),
    ("project3 - Rock Paper Scissors",      "Session 3 — Rock Paper Scissors",      820),
    ("project4 - Password Generator",       "Session 4 — Password Generator",       740),
    ("project5 - Password Strength Detector","Session 5 — Password Strength Detector",600),
    ("project6 - To-Do List",               "Session 6 — To-Do List",               560),
    ("project7 - Quiz App",                 "Session 7 — Quiz App",                 620),
    ("project8 - QR Code Generator",        "Session 8 — QR Code Generator",        720),
]

base = Path(__file__).parent

for folder, title, height in PROJECTS:
    st.subheader(title)
    html = (base / folder / "index.html").read_text(encoding="utf-8")
    components.html(html, height=height, scrolling=False)
    st.divider()
