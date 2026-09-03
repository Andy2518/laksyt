import random

def satunnainen():
    noppa = random.randint(1, 6)
    return noppa

heitot = 0

while heitot != 6:
    heitot = satunnainen()
    print(heitot)

