my_questions = [
    {
        "question_number": 1,
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "New York", "Dublin"],
        "correct_answer": "Paris",
        "explanation": "Paris is the capital and most populous city of France."
    },
    {
        "question_number": 2,
        "question": "Who is CEO of Tesla?",
        "options": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Tony Stark"],
        "correct_answer": "Elon Musk",
        "explanation": "Elon Musk is the CEO of Tesla, Inc."
    },
    {
        "question_number": 3,
        "question": "The iPhone was created by which company?",
        "options": ["Apple", "Intel", "Amazon", "Microsoft"],
        "correct_answer": "Apple",
        "explanation": "The iPhone was created by Apple Inc. and first released in 2007."
    },
    {
        "question_number": 4,
        "question": "How many Harry Potter books are there?",
        "options": ["1", "4", "6", "7"],
        "correct_answer": "7",
        "explanation": "There are 7 books in the Harry Potter series written by J.K. Rowling."
    },
    {
        "question_number": 5,
        "question": "Who wrote To Kill a Mockingbird?",
        "options": ["Harper Lee", "Stephen King", "Dan Brown", "J.K. Rowling"],
        "correct_answer": "Harper Lee",
        "explanation": "To Kill a Mockingbird was written by Harper Lee and published in 1960."
    },
    {
        "question_number": 6,
        "question": "What is the capital of Germany?",
        "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
        "correct_answer": "Berlin",
        "explanation": "Berlin is the capital and largest city of Germany."
    },
    {
        "question_number": 7,
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent Van Gogh", "Leonardo Da Vinci", "Pablo Picasso", "Claude Monet"],
        "correct_answer": "Leonardo Da Vinci",
        "explanation": "The Mona Lisa was painted by Leonardo Da Vinci in the early 16th century."
    },
    {
        "question_number": 8,
        "question": "What is the largest mammal in the world?",
        "options": ["Blue Whale", "African Elephant", "Giraffe", "Grizzly Bear"],
        "correct_answer": "Blue Whale",
        "explanation": "The Blue Whale is the largest mammal in the world, reaching lengths of up to 100 feet."
    },
    {
        "question_number": 9,
        "question": "Who is the artist of the song 'Shape of You'?",
        "options": ["Ed Sheeran", "Justin Bieber", "The Weeknd", "Drake"],
        "correct_answer": "Ed Sheeran",
        "explanation": "'Shape of You' is a song by English singer-songwriter Ed Sheeran."
    },
    {
        "question_number": 10,
        "question": "What is the currency of Brazil?",
        "options": ["Dollar", "Euro", "Real", "Peso"],
        "correct_answer": "Real",
        "explanation": "The currency of Brazil is the Brazilian Real (BRL)."
    },
    {
        "question_number": 11,
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"],
        "correct_answer": "Ottawa",
        "explanation": "Ottawa is the capital city of Canada."
    },
    {
        "question_number": 12,
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "correct_answer": "Canberra",
        "explanation": "Canberra is the capital city of Australia."
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
        # Insert "not to be displayed" at the beginning of the options list, if not already present
        if "not to be displayed" not in question["options"]:
            question["options"].insert(0, "not to be displayed")
    return(my_questions)
