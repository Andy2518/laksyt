leiviskät = int(input("Anna leiviskät:"))
naulat = int(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

g = (((leiviskät * 20) + naulat) * 32 + luodit) * 13.3
kg = g // 1000
gramma = g % 1000

print(f"Massa nykymittojen mukaan: {kg} kilogrammaa ja {gramma:.2f} grammaa.")

