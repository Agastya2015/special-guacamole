n = int(input("Enter an even number: "))
t = n
nl = 0
while t>0:
    nl = nl+1
    t = int(t/10)

if nl>=4:
    nl = int(nl/2)
    chk = 0
    while n>0:
        r = n%10
        if chk==nl:
            mo = r
        elif chk==(nl-1):
            mt = r
        n = int(n/10)
        chk = chk+1
    p = mo*mt
    print("\nProduct of mid digits (" + str(mo) + "*" + str(mt) + ") = ", p)
else:
    print("\nIt's not 4  or more than 4-digit number.")