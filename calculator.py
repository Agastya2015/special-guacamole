def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q
print("Please select operator: ")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d): ")
n1 = int(input("Please enter first number: "))
n2 = int(input("Please enter second number: "))

if choice == 'a':
    print(n1, " + ", n2, " = ", add(n1, n2))
elif choice == 'b':
    print(n1, " - ", n2, " = ", subtract(n1, n2))
elif choice == 'c':
    print(n1, " * ", n2, " = ", multiply(n1, n2))
elif choice == 'd':
    print(n1, " / ", n2, " = ", divide(n1, n2))
else:
    print("Invaild Number.")
