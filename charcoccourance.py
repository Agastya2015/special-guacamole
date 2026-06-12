s = input("Please enter your word: ")
c = input("Please enter your own character: ")
cn = 0
i = 0
while(i < len(s)):
    if(s[i] == c):
        cn = cn + 1
    i = i + 1
print("The total Number of times ", c,"has occured = ",cn)