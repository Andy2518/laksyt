import math

def pizza (halkaisija, hinta):
    metri = halkaisija / 100
    sade = metri / 2
    pinta_ala = math.pi * sade * sade
    return hinta / pinta_ala

pizza1_halkaisija = int(input("Anna ensimmäisen pizzan halkaisija:"))
pizza1_hinta = float(input("Anna ensimmäisen pizzan hinta:"))
pizza2_halkaisija = int(input("Anna toisen pizzan halkaisija:"))
pizza2_hinta = float(input("Anna toisen pizzan hinta:"))

pizza1 = pizza(pizza1_halkaisija, pizza1_hinta)
pizza2 = pizza(pizza2_halkaisija, pizza2_hinta)

if pizza1 > pizza2:
    print("Pizza2 antaa paremman vastineen rahalle.")
elif pizza1 < pizza2:
    print("Pizza1 antaa paremman vastineen rahalle.")