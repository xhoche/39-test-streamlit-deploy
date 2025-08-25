# import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )
import streamlit as st
import time
import random
import quiz

NB_QUIZ_QUESTIONS = 5

st.title('hello, this is my web page quizz')

# the below code ensures that the first radio button is not displayed
# this is to avoid displaying any selected radio button for the answer
# in order not to influence the user's choice
# this is done by adding a style tag that hides the first radio button
# the style tag is added to the page using the st.markdown function
st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            }
        </style>
        """,
    unsafe_allow_html=True
)

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

# Add space between the header and the next item
nl(1)

# Text Prompt
st.markdown("""
            Here you can write Quiz Description and Instructions, if necessary.
            """)

# Create Placeholder to print test score
scorecard_placeholder = st.empty()

# Activate Session States
ss = st.session_state
# Initializing Session States
if 'counter' not in ss:
    ss['counter'] = 0
if 'start' not in ss:
    ss['start'] = False
if 'stop' not in ss:
    ss['stop'] = False
if 'refresh' not in ss:
    ss['refresh'] = False
if "button_label" not in ss:
    ss['button_label'] = ['START', 'SUBMIT', 'RELOAD']
if 'current_quiz' not in ss:
    ss['current_quiz'] = {}
if 'user_answers' not in ss:
    ss['user_answers'] = []
if 'grade' not in ss:
    ss['grade'] = 0

# Function for button click
def btn_click():
    ss.counter += 1
    if ss.counter > 2:
        ss.counter = 0
        ss.clear()
    else:
        update_session_state()
        with st.spinner("*this may take a while*"):
            time.sleep(2)

# Function to update current session
def update_session_state():
    if ss.counter == 1:
        ss['start'] = True
        ss.current_quiz = random.sample(quiz.my_questions, NB_QUIZ_QUESTIONS)
        print(f"Current quiz will display {len(ss.current_quiz)} questions")
        ss.current_quiz = quiz.initialise_questions(ss.current_quiz)
        print("Current quiz has been initialized")
    elif ss.counter == 2:
        # Set start to False
        ss['start'] = True
        # Set stop to True
        ss['stop'] = True

# Initializing Button Text at the top of the page
st.button(label=ss.button_label[ss.counter],
        key='button_press_top', on_click= btn_click)

# Function to display a question
def quiz_app():
    # create container
    with st.container():
        if (ss.start):
            for i in range(len(ss.current_quiz)):
                number_placeholder = st.empty()
                question_placeholder = st.empty()
                options_placeholder = st.empty()
                results_placeholder = st.empty()
                expander_area = st.empty()
                # Add '1' to current_question tracking variable cause python starts counting from 0
                current_question = i+1
                # display question_number
                number_placeholder.write(f"*Question {current_question}*")
                # display question based on question_number
                question_placeholder.write(f"**{ss.current_quiz[i].get('question')}**")
                # list of options
                options = ss.current_quiz[i].get("options")
                # track the user selection
                options_placeholder.radio("", options,  key=f"Q{current_question}", index = 0)
                # Add space between the question and the next item
                nl(1)
                # Grade Answers and Return Corrections
                if ss.stop:
                    # Track length of user_answers
                    if len(ss.user_answers) < NB_QUIZ_QUESTIONS :
                        # comparing answers to track score
                        if ss[f'Q{current_question}'] == ss.current_quiz[i].get("correct_answer"):
                            ss.user_answers.append(True)
                        else:
                            ss.user_answers.append(False)
                    else:
                        pass
                    # Results Feedback
                    if ss.user_answers[i] == True:
                        results_placeholder.success("CORRECT")
                    else:
                        results_placeholder.error("INCORRECT")
                    # Explanation of the Answer
                    expander_area.write(f"*{ss.current_quiz[i].get('explanation')}*")

            # Initializing Button Text at the bottom of the page
            st.button(label=ss.button_label[ss.counter],
                    key='button_press_bottom', on_click= btn_click)


    # calculate score
    if ss.stop:
        ss['grade'] = ss.user_answers.count(True)
        scorecard_placeholder.write(f"### **Your Final Score : {ss['grade']} / {len(ss.current_quiz)}**")

# Display the quiz
quiz_app()
