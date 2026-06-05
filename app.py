import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="TUMO Workshop Projects", layout="wide")

st.title("TUMO Workshop — 8 Mini Projects")
st.markdown("As it is a live demo, you can interact with these applications right here")
st.divider()

# (folder name, display title, description, iframe height in px)
PROJECTS = [
    (
        "project1 - Digital Clock",
        "Session 1 — Digital Clock",
        "A live digital clock that reads the current time from the browser and updates every second. "
        "It displays hours, minutes, seconds, AM/PM, the day of the week, and the full date — "
        "styled with a neon green glow on a dark background.",
        600,
    ),
    (
        "project2 - Age Calculator",
        "Session 2 — Age Calculator",
        "A birthday-to-age converter that takes a date input and instantly calculates the user's "
        "exact age in years, months, and days. It also shows a fun fact: the total number of days "
        "the user has been alive.",
        680,
    ),
    (
        "project3 - Rock Paper Scissors",
        "Session 3 — Rock Paper Scissors",
        "A fully playable Rock Paper Scissors game against the computer. The player taps one of "
        "three emoji buttons, the computer makes a random choice, and the winner is announced "
        "immediately. A scoreboard keeps track of wins and losses across multiple rounds.",
        820,
    ),
    (
        "project4 - Password Generator",
        "Session 4 — Password Generator",
        "A security tool that generates a random password based on the user's preferences. "
        "Set the length with a slider, choose which character types to include, and copy the "
        "result to the clipboard with one click.",
        740,
    ),
    (
        "project5 - Password Strength Detector",
        "Session 5 — Password Strength Detector",
        "A real-time password analyser that evaluates a password as the user types. It checks "
        "five requirements and reflects each one instantly in a colour-coded checklist, while a "
        "strength bar animates from red to green as more requirements are met.",
        600,
    ),
    (
        "project6 - To-Do List",
        "Session 6 — To-Do List",
        "A fully functional task manager where users can add, complete, and delete tasks. Tasks "
        "can be filtered by status (All / Active / Completed) and are saved to localStorage so "
        "the list is preserved even after closing or refreshing the page.",
        560,
    ),
    (
        "project7 - Quiz App",
        "Session 7 — Quiz App",
        "A multiple-choice knowledge quiz spanning three screens: start, question, and results. "
        "The player works through 8 questions on tech, science, and general knowledge, with a "
        "progress bar and a personalised score message at the end.",
        620,
    ),
    (
        "project8 - QR Code Generator",
        "Session 8 — QR Code Generator",
        "A tool that converts any text or URL into a scannable QR code instantly in the browser "
        "using the qrcode.js library. The user can choose a size and download the result as a "
        "PNG image — no server or backend required.",
        720,
    ),
]

base = Path(__file__).parent

for folder, title, description, height in PROJECTS:
    st.subheader(title)
    st.write(description)
    html = (base / folder / "index.html").read_text(encoding="utf-8")
    components.html(html, height=height, scrolling=False)
    st.divider()
