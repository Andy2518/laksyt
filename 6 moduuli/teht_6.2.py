import random

def satunnainen(tahkot):
    noppa = random.randint(1, tahkot)
    return noppa

maksimiluku = int(input("Anna maksimiluku:"))
heitot = 0

while heitot != maksimiluku:
    heitot = satunnainen(maksimiluku)
    print(heitot)