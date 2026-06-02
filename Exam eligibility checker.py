m = input("Did you have a medical cause? (Y/N) : ")
if m == "Y":
    print("You are allowed to appear for the exam.")
else:
    a = int(input("Enter attendance of the student: "))
    if a >= 75 and a <= 100:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam.")
