rs = int(input("Enter number of rows: "))
if rs%2==0:
    hd = int(rs/2)
else:
    hd = int(rs/2)+1
s = hd-1
for i in range(1, hd+1):
    for j in range(1, s+1):
        print(end=" ")
    s = s-1
    n = 1
    for j in range(2*i-1):
        print(end=str(n))
        n =  n+1
    print()
s = 1
for i in range(1, hd):
    for j in range(1, s+1):
        print(end=" ")
    s = s+1
    n = 1
    for j in range(1, 2*(hd-i)):
        print(end=str(n))
        n = n+1
    print()
    
        