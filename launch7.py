import streamlit as st
import os

# Define the quiz data with scores
quiz = [
    {
        "question": "Scenario 1: Heng! Ong! Huat Ah! Your family has just won the lottery of 5 million after the Toto draw has reached 10 million! So many things that you can buy and do with the money! What would you do with the winnings…?",
        "options": [
            {"option": "A) Invest in some gold! They hold long-term value and are reliable. Won’t go wrong with this!", "score": 2},
            {"option": "B) Let’s keep our money in Fixed Deposit first! Maybe we can stick with practical things like food and basic insurance and keep the money for rainy days.", "score": 1},
            {"option": "C) Perhaps we can buy a mix of practical and fun items? We can get a new family car for daily use and a few luxury items to indulge in!", "score": 4},
            {"option": "D) Let’s buy some expensive clothes and gadgets. We never ever buy expensive things anyways! It’s always good to indulge a little.", "score": 5},
            {"option": "E) What is the rest of my family doing with the money? I’ll see what they do and perhaps follow them!", "score": 3},
            {"option": "F) Hmmm, let’s purchase items that are valuable, but also useful. A blend of gold for investment and tech gadgets for fun, sounds like a responsible choice!", "score": 6},
        ]
    },
    {
        "question": "Scenario 2: Let’s go to the beach-each!\nLet’s go on a short family trip to Bali! Someone in the family planned a trip for everybody to go to Bali together. What are you most excited for?",
        "options": [
            {"option": "A) A quiet, relaxing vacation where we can focus on unwinding, with some sightseeing but no big risks.", "score": 2},
            {"option": "B) Let’s just keep it safe in a familiar environment. We need to know everything is under control so we don’t get robbed or ill on the trip.", "score": 1},
            {"option": "C) Exciting! A balanced trip would be great. A little shopping with a little adventure with some relaxing time—maybe some snorkeling or hiking, but also a spa day.", "score": 4},
            {"option": "D) A wild adventure! Let’s go skydiving, zip-lining, and deep-sea diving. I want to try everything!", "score": 5},
            {"option": "E) I’ll see what the rest of the family is doing and I’ll follow suit! Should we go with a tour?", "score": 3},
            {"option": "F) We can research safe yet exciting places to visit so we can get the best of both worlds and also get the most value for our money.", "score": 6},
        ]
    },
    {
        "question": "Scenario 3: Let’s pack our luggage\nAbout to embark on a much-anticipated vacation, it’s time to pack! Everyone has different priorities—what do you pack in your luggage?",
        "options": [
            {"option": "A) Pack essentials first—clothes, toiletries, and anything that will keep us comfortable and prepared. I might add a few extra things, but only if they’re practical.", "score": 2},
            {"option": "B) A few outfits, toiletries, and some snacks will do. Most importantly, medication! What if we get Bali Belly?", "score": 1},
            {"option": "C) Pack a balance: essentials like clothes and toiletries, but also a few fun items like a camera or some sports gear for activities.", "score": 4},
            {"option": "D) Definitely nice clothing and accessories, I want to look good for the trip! My new digital camera too so I can capture the sights there!", "score": 5},
            {"option": "F) I’ll research the weather, the activities we’ll do, and pack accordingly—ensuring I have everything I need, but nothing unnecessary. Efficiency is key.", "score": 6},
        ]
    },
    {
        "question": "Scenario 4: You finally boarded the plane! Which seat will you go for in the side aisle?",
        "options": [
            {"option": "A) Window Seat: I want to see the flight take off and sit by the window!\nYou prefer the view and a bit of isolation to enjoy the flight in peace.", "score": 4},
            {"option": "B) Aisle Seat: I don’t want to squeeze past multiple people just to go to the toilet…\nYou like easy access to move around when needed, even if it means less comfort, more into lower risks.", "score": 2},
            {"option": "C) Middle Seat: Neither here nor there but at least I get both the convenience of going to the toilet and also the view of the sky! And at least I’m surrounded by my friends on both sides!", "score": 3},
        ]
    },
    {
        "question": "Scenario 5: Coffee, Tea, or Me?\nYou're comfortably seated on the plane to Bali, and the flight attendant comes by to take your meal order. You have a few options to choose from—what’s your choice?",
        "options": [
            {"option": "A) Choose the standard meal option: chicken and rice. It’s reliable, familiar, and I know I’ll like it.", "score": 2},
            {"option": "B) OOOO tom yum or laksa? Got to stimulate the taste buds before touching down in a new city!", "score": 5},
            {"option": "C) Let’s see what the rest orders first and maybe we can share the different meals with each other!", "score": 3},
            {"option": "D) Hmmm let’s get something with fruits, vegetables and meat in it. I’ll maybe go for something nutritious and practical since we don’t know what food choices we have available when we touch down.", "score": 6},
        ]
    },
    {
        "question": "Scenario 6: Money, Money, Money\nYou have finally touched down onto Bali! You already have some exchange currency but is Lady Luck on your side, because the exchange rate is now to your favour? What do you do?",
        "options": [
            {"option": "A) Exchange a small, fixed amount—better safe than sorry in case the rate changes again.", "score": 2},
            {"option": "B) I’ll wait until I really need to exchange money, just in case. I don’t want to take risks!", "score": 1},
            {"option": "C) Exchange some, but also leave some for later exchanges if the rate changes again.", "score": 4},
            {"option": "D) That’s such a good deal! We’ll definitely spend the money anyways, let’s exchange a larger amount now so we can take advantage of the rate!", "score": 5},
            {"option": "E) Check what everyone else is doing first—if they’re exchanging, I’ll go along with it.", "score": 3},
            {"option": "F) There may be more exchangers near our resort! We can research along the way about the best times and locations to exchange currency, so we can get both value and convenience.", "score": 6},
        ]
    },
    {
        "question": "Scenario 7: The Unexpected Visitor\nNow you’re all set to your trip, you finally are on your sweet ride to PEEK resort! However, out of nowhere, there is suddenly an unexpected visitor - a cheeky monkey - which jumps on your car! What should you do now?",
        "options": [
            {"option": "A) Stay calm, keep the windows up, and observe from a safe distance. We don’t want any surprises.", "score": 2},
            {"option": "B) Quick! Close everything and make sure we’re safe. Who knows what this monkey might do?!", "score": 1},
            {"option": "C) Snap a few photos and let the monkey hang around for a bit—what a fun surprise!", "score": 4},
            {"option": "D) Ooooooh I got this Gado Gado from near the airport. Should we open the windows and give it a snack? It’s not everyday you get this close to a wild monkey!", "score": 5},
            {"option": "E) The monkey isn’t leaving the car! What should I do? Maybe the locals here have advice, let me call the staff at the resort and check what’s best to do in this situation.", "score": 6},
        ]
    },
    {
        "question": "Scenario 8: Let’s go on an adventure!\nOutside PEEK resort, a local tour guide intercepts you and offers you an Alpaca Farm package which is lower than the market rate! Should we go?",
        "options": [
            {"option": "A) Wow it’s a steal but are there cheaper options out there?", "score": 2},
            {"option": "B) Hmm, I’m worried there’s a hidden cost. I’ll double-check with the guide to make sure we don’t overspend.", "score": 1},
            {"option": "C) Fantastic! A little adventure won’t hurt—I’ll enjoy it but I’ll stay mindful of what’s not included in the package.", "score": 4},
            {"option": "D) Definitely yes! It’s outside of PEEK resort so it should be reliable! Also I’ve heard of this travel agency before so it should be fine.", "score": 5},
            {"option": "E) What does the rest think? I don’t mind going for it, sounds fun! But if they aren’t interested I’m fine doing other activities as well.", "score": 3},
            {"option": "F) Hmmm, I’ll take the tour guide’s contact and take some time to research the package more to have a worth it memorable experience without any hidden charges!", "score": 6},
        ]
    },
    {
        "question": "Scenario 9: There’s nothing like retail therapy\nSoon, it’s going to be your last day in Bali, and you’re on the hunt for souvenirs to bring back for your friends and family. The local market is bustling, and there are so many choices! What catches your eye?",
        "options": [
            {"option": "A) Let’s just mass buy these elephant pants or keychains so all my friends can get something each without having the need to compare!", "score": 2},
            {"option": "B) I think I’ll skip souvenirs and save my money. They’re nice to have, but not necessary, and I’d rather be safe than overspend.", "score": 1},
            {"option": "C) A mix of practical and fun items: maybe some handmade jewelry, a small bottle of Balinese spices, and a keychain for each friend. Something for everyone!", "score": 4},
            {"option": "D) Let’s go big! Let’s get rare items like elephant tusks, scarves, figurines, exotic coffee, and anything eye-catching that expresses that it’s from Bali.", "score": 5},
            {"option": "E) Maybe I’ll see what the locals or my family recommend, especially if there’s a popular item everyone’s buying. I want the trendiest souvenirs to give my friends!", "score": 3},
            {"option": "F) I’ll look for classic Balinese handicrafts—like wood carvings or batik cloth. Timeless, traditional, and meaningful and these will be high-quality keepsakes for my friends!", "score": 6},
        ]
    },
    {
        "question": "Scenario 10: Was it all a dream?\nAnd we're back again. After a busy trip, you deserve some rest! How do you prefer to unwind after that exciting trip to Bali?",
        "options": [
            {"option": "A) Curling up with a good book or an engaging movie sounds like the perfect way to recharge.", "score": 2},
            {"option": "B) Let’s not spend too much… I’ve already spent so much on the trip! Relaxing at home is just fine for me.", "score": 1},
            {"option": "C) A nice dinner out or a quiet day at the park is a good balance of fun and relaxation.", "score": 4},
            {"option": "D) Spa day or concert tickets—something indulgent and thrilling to end things on a high note!", "score": 5},
            {"option": "E) I’ll ask my friends or family what they’re planning and go with the flow—spending time together is the most relaxing part.", "score": 3},
            {"option": "F) I’ll choose a budget-friendly but enjoyable activity to recharge mindfully, maybe a nature walk or DIY spa night.", "score": 6},
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
        "image": "images/2.png"
    },
    {
        "name": "PEEKachu",
        "min_score": 20,
        "max_score": 29,
        "description": "You are practical and prefer familiar experiences. Safety is your top priority.",
        "image": "images/1.png"
    },
    {
        "name": "SpongePEEK",
        "min_score": 30,
        "max_score": 39,
        "description": "You tend to go with the flow and enjoy following trends with your peers.",
        "image": "images/5.png"
    },
    {
        "name": "PEEKa Pig",
        "min_score": 40,
        "max_score": 49,
        "description": "You enjoy a balanced life with a mix of fun and practicality.",
        "image": "images/3.png"
    },
    {
        "name": "PEEKzilla",
        "min_score": 50,
        "max_score": 59,
        "description": "You are adventurous and love taking risks. Thrill and excitement drive you.",
        "image": "images/4.png"
    },
    {
        "name": "PEEK.E",
        "min_score": 60,
        "max_score": 70,
        "description": "You are informed and balanced, making decisions based on research and facts.",
        "image": "images/6.png"
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
        cols[2].button("Submit", on_click=show_results)

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
