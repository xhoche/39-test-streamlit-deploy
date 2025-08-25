import pandas as pd
import random
import os

FILE_NAME = "CapitalCurrenciesLanguages2025FilledByMistralAI.xlsx"
INITIAL_FILE_PATH = os.path.join("data", FILE_NAME)

# let's load up the file into a pandas dataframe
file_path = INITIAL_FILE_PATH
my_knowledge_df = pd.read_excel(file_path,index_col=0)

continent_to_focus_on = 'Europe'
initial_info_type_provided = 'Country_Name'
knowledge_to_focus_on = 'Capital'

questions_df = my_knowledge_df[my_knowledge_df['Continent']==continent_to_focus_on]
print(len(questions_df))

my_questions = [
    {
        "question_number": 1,
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "New York", "Dublin"],
        "correct_answer": "Paris"
    }]

# when initializing the list of questions, add a new key-value pair to each dictionary
# in the list
# Iterate over each dictionary in the list
# returns the list of questions with the added option "not to be displayed" at the beginning
# of the options list
# indeed, we will later hide the first option in the radio button
# to avoid displaying any selected radio button for the answer
for question in my_questions:
    # Insert "not to be displayed" at the beginning of the options list, if not already present
    if "not to be displayed" not in question["options"]:
        question["options"].insert(0, "not to be displayed")
