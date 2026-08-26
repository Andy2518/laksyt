import random

satunnaisuus = random.randint(1, 10)
arvaus = 0

while satunnaisuus != arvaus:
    arvaus = int(input("Anna luku:"))

    if arvaus > satunnaisuus:
        print("Liian suuri arvaus!")
    elif arvaus < satunnaisuus:
        print("Liian pieni arvaus!")
    elif arvaus == satunnaisuus:
        print("Oikein!")
        break
