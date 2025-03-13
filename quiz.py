my_questions = [
    {
        "question_number": 1,
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "New York", "Dublin"],
        "correct_answer": "Paris"
    },
    {
        "question_number": 2,
        "question": "Who is CEO of Tesla?",
        "options": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Tony Stark"],
        "correct_answer": "Elon Musk"
    },
    {
        "question_number": 3,
        "question": "The iPhone was created by which company?",
        "options": ["Apple", "Intel", "Amazon", "Microsoft"],
        "correct_answer": "Apple"
    },
    {
        "question_number": 4,
        "question": "How many Harry Potter books are there?",
        "options": ["1", "4", "6", "7"],
        "correct_answer": "7"
    },
    {
        "question_number": 5,
        "question": "Who wrote To Kill a Mockingbird?",
        "options": ["Harper Lee", "Stephen King", "Dan Brown", "J.K. Rowling"],
        "correct_answer": "Harper Lee"
    },
    {
        "question_number": 6,
        "question": "What is the capital of Germany?",
        "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
        "correct_answer": "Berlin"
    },
    {
        "question_number": 7,
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent Van Gogh", "Leonardo Da Vinci", "Pablo Picasso", "Claude Monet"],
        "correct_answer": "Leonardo Da Vinci"
    },
    {
        "question_number": 8,
        "question": "What is the largest mammal in the world?",
        "options": ["Blue Whale", "African Elephant", "Giraffe", "Grizzly Bear"],
        "correct_answer": "Blue Whale"
    },
    {
        "question_number": 9,
        "question": "Who is the artist of the song 'Shape of You'?",
        "options": ["Ed Sheeran", "Justin Bieber", "The Weeknd", "Drake"],
        "correct_answer": "Ed Sheeran"
    },
    {
        "question_number": 10,
        "question": "What is the currency of Brazil?",
        "options": ["Dollar", "Euro", "Real", "Peso"],
        "correct_answer": "Real"
    },
    {
        "question_number": 11,
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"],
        "correct_answer": "Ottawa"
    },
    {
        "question_number": 12,
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "correct_answer": "Canberra"
    }
]

# when initializing the list of questions, add a new key-value pair to each dictionary
# in the list
# Iterate over each dictionary in the list
# returns the list of questions with the added option "not to be displayed" at the beginning
# of the options list
# indeed, we will later hide the first option in the radio button
# to avoid displaying any selected radio button for the answer
def initialise_questions(my_questions):
    for question in my_questions:
        # Insert "not to be displayed" at the beginning of the options list
        question["options"].insert(0, "not to be displayed")
    return(my_questions)
