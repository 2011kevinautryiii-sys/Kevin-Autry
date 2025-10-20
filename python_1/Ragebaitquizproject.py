import random

wrong_answer_insults = ("WRONG ANSWER DUMBASS!", "HOW DO YOU FUNCTION DAILY?", "OH MY GOD, YOU'RE AN IDIOT.", "IM LOSING BRAINCELLS SEEING YOURS!", "dude. you had one job. get the easiest question right.", "IDIOT IDIOT IDIOT IDIOT IDIOT", "WROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONG!")

print("answer these questions for a big reward, you fail if you get one wrong, and once that happens, NO RETURN.")

answer1 = input("""Question 1: What is the name of the creator of this quiz?
1: Kevin Autry
2: The Government
3: DAE
4: I don't know
Please Answer: """)
if answer1 == "1":
    print("oh wow, you do know me, huh? anyways dont celebrate yet. this is question 1 of many more.")
elif answer1 == "2":
    print(random.choice(wrong_answer_insults))
    exit()
elif answer1 == "3":
    print("ITS A STUDENT, IDIOT! WROOOOOOOOOOOOOOOONG!")
    exit()
elif answer1 == "4":
    print(random.choice(wrong_answer_insults))
    exit()
else:
    print("what? just put the number, dude. also WRONG ANSWER!")
    exit()
#the quiz exits on purpose
#the quiz does not tell the player what the inputs are on purpose
#these things happen because its made to make the player
answer2 = input("""Question 2: Why are you taking this quiz?
1: For fun
2: Because Kevin Autry told me to
3: I don't know
Please Answer: """)