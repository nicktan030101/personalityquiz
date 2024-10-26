import streamlit as st

# Sample Quiz Data with Scoring
quiz = [
    {
        "question": "What's your favorite color?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "scores": [10, 20, 30, 40],
        
    },
    {
        "question": "Which animal do you like the most?",
        "options": ["Cat", "Dog", "Bird", "Fish"],
        "scores": [20, 40, 10, 30],
        
    },
    # Add more questions as needed
]

# Initialize Session State
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

def restart_quiz():
    st.session_state.question_index = 0
    st.session_state.responses = [None] * len(quiz)
    st.session_state.total_score = 0

def calculate_score():
    total_score = 0
    for i, response in enumerate(st.session_state.responses):
        if response is not None:
            option_index = quiz[i]['options'].index(response)
            total_score += quiz[i]['scores'][option_index]
    st.session_state.total_score = total_score

def show_results():
    calculate_score()
    st.markdown("## Your Results")
    st.write(f"**Total Score:** {st.session_state.total_score}")
    # Personalized message based on score
    if st.session_state.total_score <= 50:
        st.write("You are calm and collected!")
    elif st.session_state.total_score <= 80:
        st.write("You are energetic and lively!")
    else:
        st.write("You are adventurous and bold!")
    st.button("Restart Quiz", on_click=restart_quiz)

def show_question():
    index = st.session_state.question_index
    question = quiz[index]

    # Display Progress Bar
    progress = (index + 1) / len(quiz)
    st.progress(progress)

    # Display Image
    #st.image(question['image'], use_column_width=True)

    # Display Question
    st.markdown(f"### {question['question']}")

    # Display Options
    options = question['options']
    response = st.radio("Select an option:", options, index=options.index(st.session_state.responses[index]) if st.session_state.responses[index] else 0, key=index)

    # Save the response
    st.session_state.responses[index] = response

    # Navigation Buttons
    cols = st.columns(3)
    if index > 0:
        cols[0].button("Previous", on_click=previous_question)
    if index < len(quiz) - 1:
        cols[2].button("Next", on_click=next_question)
    else:
        cols[2].button("Submit", on_click=show_results)

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

    st.title("🌟 Personality Quiz")
    show_question()

if __name__ == "__main__":
    main()
