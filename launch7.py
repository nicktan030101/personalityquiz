import streamlit as st
import os
import urllib.parse  # For URL encoding

# Define the quiz data with scores
quiz = [
    {
        "question": "Scenario 1: Congratulations, You've just won the $5 million lottery! What are you going to do with all that money?",
        "options": [
            {"option": "A) Invest in some gold!", "score": 2},
            {"option": "B) Keep your money in a fixed deposit account", "score": 1},
            {"option": "C) Indulge a little! Buy a new family car and a few luxury goods", "score": 4},
            {"option": "D) Indulge a lot! Buy the newest gadgets, clothes, and jewelry", "score": 5},
            {"option": "E) Do what my friends are doing with their money", "score": 3},
            {"option": "F) Buy some gold and some gadgets to indulge a bit", "score": 6},
        ]
    },
    {
        "question": "Scenario 2: You've decided to use that money to go to Bali with your family! What are you most looking forward to?",
        "options": [
            {"option": "A) A quiet relaxing vacation with some sightseeing.", "score": 2},
            {"option": "B) I'm not looking forward to much; going overseas is dangerous!", "score": 1},
            {"option": "C) A little adventure but also some time to relax and unwind", "score": 4},
            {"option": "D) All-out adventure, whatever gets the heart pumping!", "score": 5},
            {"option": "E) Whatever my family wants to do", "score": 3},
            {"option": "F) I'd need to do some research first—something fun and relaxing but not too expensive", "score": 6},
        ]
    },
    {
        "question": "Scenario 3: Time to pack! What are you packing?",
        "options": [
            {"option": "A) Essentials first, then a few practical non-essentials if there's still room", "score": 2},
            {"option": "B) All the essentials, especially MEDICINE—what if we get Bali belly?", "score": 1},
            {"option": "C) Essentials and some fun items like a camera and sports gear", "score": 4},
            {"option": "D) All of my nicest clothes, jewelry, and new camera!", "score": 5},
            {"option": "E) Whatever else everyone else is packing", "score": 3},
            {"option": "F) I'll need to research the location and make my decisions based on that so I don't bring anything unnecessary", "score": 6},
        ]
    },
    {
        "question": "Scenario 4: We've managed to get free seat selection! What seat are you picking?",
        "options": [
            {"option": "A) Window Seat", "score": 4},
            {"option": "B) Aisle Seat", "score": 2},
            {"option": "C) Middle Seat", "score": 3},
        ]
    },
    {
        "question": "Scenario 5: We're on the plane! The flight attendant asks for your meal order; what do you pick?",
        "options": [
            {"option": "A) Chicken and rice, something familiar that can't go wrong!", "score": 2},
            {"option": "B) Chicken porridge—let's not risk upsetting our stomach before the holiday.", "score": 1},
            {"option": "C) Tom yum or laksa—let's spice things up and get something good before the holiday starts for real!", "score": 4},
            {"option": "D) Is there champagne? It's time to party!", "score": 5},
            {"option": "E) I'll get whatever the rest get.", "score": 3},
            {"option": "F) I heard nasi goreng is a local Balinese dish that isn't too harsh on the stomach; let's get that!", "score": 6},
        ]
    },
    {
        "question": "Scenario 6: You have finally touched down in Bali! You already have some exchanged currency, but Lady Luck is on your side because the exchange rate is now in your favor. What do you do?",
        "options": [
            {"option": "A) Exchange about half of the cash and leave the other half in case the rate gets better", "score": 2},
            {"option": "B) Exchange all our money; it's such a good deal, and what if there's an emergency situation? We need it!", "score": 1},
            {"option": "C) Exchange a small amount first—who knows if the rate is gonna get better", "score": 4},
            {"option": "D) I won't convert any money; let's hope the rate gets even better!", "score": 5},
            {"option": "E) I'll do what everyone else does", "score": 3},
            {"option": "F) Let's search if there are more exchanges near our resort first and see if there are any with better rates!", "score": 6},
        ]
    },
    {
        "question": "Scenario 7: We've reached the resort, finally! A monkey suddenly appears on the balcony outside of one of the rooms; what are you doing?",
        "options": [
            {"option": "A) Stay calm, close the door to the balcony, and keep an eye on it.", "score": 2},
            {"option": "B) EMERGENCY! Close all the doors, call for a family meeting on how to deal with the monkey—what if it's venomous?!", "score": 1},
            {"option": "C) Snap some photos and just let it do its thing.", "score": 4},
            {"option": "D) Let's have some fun and feed it some food!", "score": 5},
            {"option": "E) Go with the flow and see what everyone else does.", "score": 3},
            {"option": "F) Maybe the locals have advice; let me call the staff at the resort and check what's best to do in this situation.", "score": 6},
        ]
    },
    {
        "question": "Scenario 8: It's time to go out! On the way out of the resort, a tour guide approaches you and offers you an Alpaca farm package he says is below market-rate! Shall we?",
        "options": [
            {"option": "A) What a good deal! I wonder if there are better deals out there though...", "score": 2},
            {"option": "B) Let's not go; I'm not going to trust a stranger!", "score": 1},
            {"option": "C) Amazing! Let's go, but be careful not to fall for any hidden costs.", "score": 4},
            {"option": "D) LET'S GO!!! He looks like a tour guide, so this must be legit.", "score": 5},
            {"option": "E) Let's see what the rest think.", "score": 3},
            {"option": "F) Let's get his contact and get back to him. In the meantime, do some research online before making a decision.", "score": 6},
        ]
    },
    {
        "question": "Scenario 9: It's the last day of what's been an awesome holiday, and we're out souvenir hunting for friends at the local market. What are you getting?",
        "options": [
            {"option": "A) Mass buy some elephant pants or keychains so that everyone gets the same thing.", "score": 2},
            {"option": "B) Nothing; I need to be smart with my money.", "score": 1},
            {"option": "C) A mix of practical and fun items—maybe some handmade jewelry and keychains.", "score": 4},
            {"option": "D) Let's splurge! Exotic spices and expensive unique jewelry.", "score": 5},
            {"option": "E) Whatever everyone else gets or whatever is the most popular souvenir.", "score": 3},
            {"option": "F) Find out what the most unique and thoughtful yet practical thing Bali has to offer and get it!", "score": 6},
        ]
    },
    {
        "question": "Scenario 10: Aaaaand we're back to reality; the holiday is over. What are you doing now that you're back home?",
        "options": [
            {"option": "A) A simple dinner with my friends to catch up.", "score": 2},
            {"option": "B) Relax at home... I need to save money after that holiday.", "score": 1},
            {"option": "C) A nice dinner out with my friends to catch up.", "score": 4},
            {"option": "D) Go for a spa day or buy the latest concert tickets; let's end off the week with a final bang.", "score": 5},
            {"option": "E) I'll ask my friends and family what they're up to and follow suit.", "score": 3},
            {"option": "F) Choose a budget-friendly yet enjoyable way to unwind and relax—perhaps a DIY spa day?", "score": 6},
        ]
    },
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

def add_social_share_buttons(share_message):
    st.markdown("---")
    st.markdown("### Share your results:")

    # Encode the share message for URLs
    encoded_message = urllib.parse.quote(share_message)

    # Social media share URLs
    twitter_url = f"https://twitter.com/intent/tweet?text={encoded_message}"
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://peek.money/"
    linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url=https://peek.money/"
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_message}"
    # Since Instagram doesn't support direct URL sharing, we'll provide a link to the Instagram profile
    instagram_url = "https://www.instagram.com/your_instagram_profile/"

    # Display Buttons
    st.markdown(f"""
    <div style='text-align: center;'>
        <a href='{twitter_url}' target='_blank' style='margin-right: 10px;'>
            <img src='https://img.icons8.com/color/48/000000/twitter--v1.png' alt='Twitter' width='48'>
        </a>
        <a href='{facebook_url}' target='_blank' style='margin-right: 10px;'>
            <img src='https://img.icons8.com/color/48/000000/facebook-new.png' alt='Facebook' width='48'>
        </a>
        <a href='{linkedin_url}' target='_blank' style='margin-right: 10px;'>
            <img src='https://img.icons8.com/color/48/000000/linkedin.png' alt='LinkedIn' width='48'>
        </a>
        <a href='{whatsapp_url}' target='_blank' style='margin-right: 10px;'>
            <img src='https://img.icons8.com/color/48/000000/whatsapp.png' alt='WhatsApp' width='48'>
        </a>
        <a href='{instagram_url}' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/instagram-new.png' alt='Instagram' width='48'>
        </a>
    </div>
    """, unsafe_allow_html=True)

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
        # Create a shareable message
        share_message = f"I just took the Peek Personality Quiz and I'm {character['name']}! 🎉 Find out which character you are at https://peek.money/"
    else:
        st.write("No character matched your score.")
        share_message = "I just took the Peek Personality Quiz! Try it yourself at https://peek.money/."

    # Add Call to Action
    st.markdown("---")
    st.markdown("**Want to explore more? Visit our [official website](https://peek.money/) for more financial tips and solutions!**")

    # Add Social Media Share Buttons
    add_social_share_buttons(share_message)

     st.markdown("<br><br>", unsafe_allow_html=True)
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
