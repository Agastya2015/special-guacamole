print("Welcome to the number guessing game!")
print("You have only 5 attempts to guess the number!")
print("Are you ready...?")
n =  int(input("\nEnter a number: "))
import random
n = random.randint(1, 100)
a = 5
while a > 0:
    g = int(input("\n guess the number: "))
    if g == n:
        print("Congratulations🎉! You won!")
        break
    else:
        a = a - 1
        if g < n:
            d = n - g 
        else:
            d = g - n
            if d >= 20:
                print("🧊 Ice cold!")
            elif d >= 10:
                print("❄️ Cold!")
            elif d >= 5:
                print("🌡️ Warm!")
            else:
                print("🔥 Hot!")
        print("Lives left: ", end="")
        for i in range(a):
            print("❤️", end="")
        print()
        if a == 0:
            print("💥💥Game over!! You ran out of lives!!")
            print("The number was: ", n)
    

    