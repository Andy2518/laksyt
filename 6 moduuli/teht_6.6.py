import math

def pizza (halkaisija, euro):
    sade = halkaisija / 2
    metri = sade / 100
    pinta_ala = math.pi * (metri**2)
    euro / pinta_ala
    return euro

pizza1_halkaisija = int(input("Anna ensimmäisen pizzan halkaisija:"))
pizza1_hinta = float(input("Anna ensimmäisen pizzan hinta:"))
pizza2_halkaisija = int(input("Anna toisen pizzan halkaisija:"))
pizza2_hinta = float(input("Anna toisen pizzan hinta:"))

pizza1 = pizza(pizza1_halkaisija, pizza1_hinta)
pizza2 = pizza(pizza2_halkaisija, pizza2_hinta)

if pizza1 > pizza2:
    print("Pizza1 antaa paremman vastineen rahalle.")
elif pizza1 < pizza2:
    print("Pizza2 antaa paremman vastineen rahalle.")