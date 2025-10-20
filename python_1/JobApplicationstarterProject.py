age = int(input("Enter your age: "))
name = input("Enter your name: ")
#Job application
if age >= 18:
    print("hello", name, "you are old enough for this job.")
    print("Choose why you want this job:")
    print("1. I need that money!")
    print("2. I want to help people!")
    print("3. I want to to do what i love!")
    job_choice = input("Enter the number of your chosen job: ")
    if job_choice == "1":
        print("well i respect the hustle, but thats not what i wanna hear. get out of my sight.")
        print("you are not hired.")
    elif job_choice == "2":
        print("Thats nice! you are hired! welcome to the team,", name)
    elif job_choice == "3":
        print("I respect you for that, but remember there is more to this job than doing what you want. but other than that, you are eligible! welcome to the team,", name)
    else:
        print("Invalid choice.")
else:
    print("sorry", name, "you are not old enough for this job.") 
    print("you are not hired.")
#End of job application