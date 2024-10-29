import streamlit as st
import os

# Define the quiz data with scores
quiz = [
    {
        "question": "Scenario 1: Heng! Ong! Huat Ah! Your family has just won the lottery of 5 million after the Toto draw has reached 10 million! So many things that you can buy and do with the money! What would you do with the winnings…?",
        "options": [
            {"option": "A) Invest in some gold! They hold long-term value and are reliable. Won't go wrong with this!", "score": 2},
            {"option": "B) Let's keep our money in Fixed Deposit first! Maybe we can stick with practical things like food and basic insurance and keep the money for rainy days.", "score": 1},
            {"option": "C) Perhaps we can buy a mix of practical and fun items? We can get a new family car for daily use and a few luxury items to indulge in!", "score": 4},
            {"option": "D) Let's buy some expensive clothes and gadgets. We never ever buy expensive things anyways! It's always good to indulge a little.", "score": 5},
            {"option": "E) What is the rest of my family doing with the money? I'll see what they do and perhaps follow them!", "score": 3},
            {"option": "F) Hmmm, let's purchase items that are valuable, but also useful. A blend of gold for investment and tech gadgets for fun sounds like a responsible choice!", "score": 6},
        ]
    },
    # ... (Rest of your quiz data, make sure to use double quotes and check for single quotes within strings)
]

# Character outcomes based on total score
character_outcomes = [
    {
        "name": "MoPEEKo",
        "min_score": 10,
        "max_score": 19,
        "description": "You are cautious and prefer to avoid risks. You value security and stability.",
        "image": "2.png"
    },
    {
        "name": "PEEKachu",
        "min_score": 20,
        "max_score": 29,
        "description": "You are practical and prefer familiar experiences. Safety is your top priority.",
        "image": "1.png"
    },
    {
        "name": "SpongePEEK",
        "min_score": 30,
        "max_score": 39,
        "description": "You tend to go with the flow and enjoy following trends with your peers.",
        "image": "5.png"
    },
    {
        "name": "PEEKa Pig",
        "min_score": 40,
        "max_score": 49,
        "description": "You enjoy a balanced life with a mix of fun and practicality.",
        "image": "3.png"
    },
    {
        "name": "PEEKzilla",
        "min_score": 50,
        "max_score": 59,
        "description": "You are adventurous and love taking risks. Thrill and excitement drive you.",
        "image": "4.png"
    },
    {
        "name": "PEEK.E",
        "min_score": 60,
        "max_score": 70,
        "description": "You are informed and balanced, making decisions based on research and facts.",
        "image": "6.png"
    },
]

# Initialize Session State
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.responses = [None] * len(quiz)
    st.session_state.total_score = 0

def next_question():
    if st.session_state.responses[st.session_state.question_index] is not None:
        st.session_state.question_index += 1
    else:
        st.warning("Please select an answer before proceeding.")

def previous_question():
    st.session_state.question_index -= 1

def submit_quiz():
    if st.session_state.responses[st.session_state.question_index] is not None:
        st.session_state.question_index += 1
    else:
        st.warning("Please select an answer before submitting.")

def restart_quiz():
    st.session_state.quiz_started = False
    st.session_state.question_index = 0
    st.session_state.responses = [None] * len(quiz)
    st.session_state.total_score = 0

def calculate_score():
    total_score = 0
    for i, response in enumerate(st.session_state.responses):
        if response is not None:
            # Find the selected option
            for option in quiz[i]['options']:
                if option['option'] == response:
                    total_score += option['score']
                    break
    st.session_state.total_score = total_score

def show_results():
    calculate_score()
    st.markdown("## Your Results")
    # Determine the character based on total score
    total_score = st.session_state.total_score
    character = None
    for outcome in character_outcomes:
        if outcome['min_score'] <= total_score <= outcome['max_score']:
            character = outcome
            break
    if character:
        st.write(f"### You are {character['name']}!")
        st.write(character['description'])
        if character['image']:
            st.image(character['image'], use_column_width=True)
    else:
        st.write("No character matched your score.")
    st.button("Restart Quiz", on_click=restart_quiz)

def show_question():
    index = st.session_state.question_index
    question = quiz[index]

    # Display Progress Bar
    progress = (index + 1) / len(quiz)
    st.progress(progress)

    # Display Question
    st.markdown(f"### {question['question']}")

    # Display Options
    options = [opt['option'] for opt in question['options']]
    if st.session_state.responses[index] is not None:
        current_selection = options.index(st.session_state.responses[index])
        response = st.radio(
            "Select an option:",
            options,
            index=current_selection,
            key=str(index)
        )
    else:
        response = st.radio(
            "Select an option:",
            options,
            key=str(index)
        )

    # Save the response
    st.session_state.responses[index] = response

    # Navigation Buttons
    cols = st.columns(3)
    if index > 0:
        cols[0].button("Previous", on_click=previous_question)
    if index < len(quiz) - 1:
        cols[2].button("Next", on_click=next_question)
    else:
        cols[2].button("Submit", on_click=submit_quiz)

def show_landing_page():
    st.title("🌟 Welcome to the Peek Personality Quiz!")
    st.image("Instagram Post design.png", use_column_width=True)
    st.markdown("""
    **Discover which 'Peek' character you are by answering a series of fun scenarios!**

    - **Instructions**:
        - You'll be presented with a series of scenarios.
        - Choose the option that best describes what you would do.
        - At the end, you'll find out which character matches your personality!

    **Ready to begin?**
    """)
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True

def main():
    # Custom CSS for Responsive Design
    st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
            width: 100%;
        }
        .stProgress > div > div > div > div {
            background-color: #4CAF50;
        }
    </style>
    """, unsafe_allow_html=True)

    if not st.session_state.quiz_started:
        show_landing_page()
    elif st.session_state.question_index < len(quiz):
        show_question()
    else:
        show_results()

if __name__ == "__main__":
    main()
