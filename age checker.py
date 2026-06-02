a = int(input("Enter your REAL age: "))
if a <= 10:
    print("You are still a child.")
elif a <= 13:
    print("You are a teenager.")
elif a <= 20:
    print("You are legally an adult.")
elif a <= 40:
    print("You are a middle-aged person.")
elif a <= 60:
    print("You are a senior citizen.")
else:
    print("Please enter your correct age.")