#Pyydetään kaksi syötettä, jotta voitaisiin laskea ne.
numero1 = int(input("Anna numero:"))
numero2 = int(input("Anna numero:"))

# Lasketaan summa, tulo ja keskiarvo.
summa = numero1 + numero2
tulo = numero1 * numero2
keskiarvo = numero1 + numero2 / 2

#Tulostetaan edellisen rivin vastaukset.
print(f"Summa on {summa}")
print(f"Tulo on {tulo}")
print(f"Keskiarvo on {keskiarvo}")