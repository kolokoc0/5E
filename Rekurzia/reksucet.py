vysledok = 0
def reksucin(a,b):
    global vysledok
    if a ==0:
        return vysledok
    else:
        a -=1
        vysledok +=b
        return reksucin(a,b)
print(reksucin(7,6))


def reksucet(a,b):
    if a==0:
        return b
    else:
        return reksucet(a-1,b)

print(reksucet(7,6))
