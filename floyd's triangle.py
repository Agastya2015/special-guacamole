r = int(input("Enter total no. of rows: "))
n = 1
print("\nFloyd's Triangle: ")
for i in range(1, r +1):
    for j in range(1, i + 1):
        print(n, end= " ")
        n = n + 1
    print()
