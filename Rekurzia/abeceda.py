from string import ascii_lowercase
n = 3
vysledok = []
for i in range(0,n):
    vysledok.append("a")

def genhes(n):
    if n ==0:
        print(vysledok)
    else:
        for pis in ascii_lowercase:
            vysledok[n*(-1)] = pis
            genhes(n-1)

print(genhes(n))
