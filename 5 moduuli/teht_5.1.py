import random

arpakuutio = int((input("Anna lukumäärä:")))
summa = 0

for i in range(arpakuutio):
    arpa = random.randint(1,6)
    summa += arpa
print(summa)
