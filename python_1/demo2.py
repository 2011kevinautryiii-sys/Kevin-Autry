import random

# List of insult messages (list of strings)
wrong_answer_insults = [
    "WRONG ANSWER DUMBASS!",
    "HOW DO YOU FUNCTION DAILY?",
    "OH MY GOD, YOU'RE AN IDIOT.",
    "I'M LOSING BRAINCELLS SEEING YOURS!",
    "Dude. You had one job. Get the easiest question right.",
    "IDIOT IDIOT IDIOT IDIOT IDIOT",
    "WROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONG!"
]

# Float to track player IQ points
player_iq = 0.0

# Function to insult user randomly and end game
def fail_quiz():
    """Ends the quiz immediately with a random insult."""
    print(random.choice(wrong_answer_insults))
    exit()

# Function to ask a question and check the answer
def ask_question(question_text, correct_answer):
    """Displays a question, takes input, and checks against the correct answer."""
    user_response = input(question_text)
    if user_response == correct_answer:
        print("yeah, no duh... next question!")
        return True
    elif user_response not in ["1", "2", "3", "4"]:
        print("what? just put the number, dude. also WRONG ANSWER!")
        fail_quiz()
    else:
        fail_quiz()

# Introduction
print("Answer these questions for a big reward. You fail if you get one wrong — NO RETURN.")

# Create a list of tuples (question, correct answer)
quiz_questions = [
    ("""Question 1: What is the name of the creator of this quiz?
1: Kevin Autry
2: The Government
3: DAE
4: I don't know
Please Answer: """, "1"),

    ("""Question 2: Why are you taking this quiz?
1: Cuz I volunteered, duhhhhh
2: Because DAE told me to
3: For the prize
4: This is multiple choice right? So how am I supposed to answer otherwise?
Please Answer: """, "3"),

    ("""Question 3: 6 + 7 = what? (Hint: it's 13)
1: SIX SEVENNNNNN
2: -1
3: 13
4: 67
Please Answer: """, "2"),  # trick question!
]

# Loop through questions
for question_text, correct_answer in quiz_questions:
    if ask_question(question_text, correct_answer):
        player_iq += 1

# Custom question without multiple choice
def final_question():
    """Handles the final, open-ended question."""
    user_response = input("""Final Question: What is the color of the sky?
1: Blue
2: Green
3: Kevin
4: It depends on the atmospheric conditions
OR you can just type the actual color: """)

    if user_response.lower() == "sky":
        print("YEAH NO DUH, THE COLOR OF THE SKY IS SKY. YOU WIN NOTHING, HAHA NERD.")
    else:
        fail_quiz()

# Call final question
final_question()

print(f"Congratulations! Your final IQ score is {player_iq}. (Spoiler: it’s still not great.)")
