print("answer these questions for a big reward, you fail if you get one wrong")
answer1 = input('Question 1: what is the name of the creator of this quiz? (1: Kevin Autry, 2: The Government, 3: DAE, 4: i dont know)\nPlease Answer): ')
if answer1 == "1":
    print("Correct, you do know me, huh?")
elif answer1 == "2":
    print("WRONG ANSWER, DUMBASS!")
    exit()
elif answer1 == "3":
    print("ITS A STUDENT, IDIOT!")
    exit()
elif answer1 == "4":
    print("TOO BAD!")
    exit
else:
    print("what? just put the number, dude. also WRONG ANSWER!")
    exit()
#the quiz exits on purpose
#the quiz does not tell the player inputs on purpose
print("Question 2: ")