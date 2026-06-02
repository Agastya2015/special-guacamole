u = int(input("Enter number of units consumed: "))
if (u < 50):
    a = u * 2.60
    s = 25
elif (u <= 100):
    a = 130 + ((u - 50) * 3.25)
    s = 35
elif (u <= 200):
    a = 130 + 162.50 + ((u -100) * 5.26)
    s = 45
else:
    a = 130 + 162.50 + 526 + ((u - 200) * 8.45)
    s = 75

t = a + s
print("\nElectricty bill =  %.2f" %t)
    
