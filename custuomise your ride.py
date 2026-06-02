print("Select you ride: ")
print("1. Bike")
print("2. Car")

c = int(input("Enter your choice: "))
if c == 1:
    print("what type of bike do you want?")
    print("1. Scooty\n")
    print("2. Scooter\n")

    c2 = int(input("Enter choice 2: "))
    if c2 == 1:
        print("you have selected scooty.")
    else:
        print("You have selected scooter.")
elif c == 2:
    print("What type of car do you want?")
    print("1. Sedan\n")
    print("2. XUV\n")

    c3 = int(input("Enter choice 3: "))
    if c3 == 1:
        print("you have selected sedan")
    else:
        print("you have selected XUV")
else:
    print("Wrong choice!")
