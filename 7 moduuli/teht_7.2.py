nimet = set()
syote = input("Anna nimi: ")

while syote != "":
    if syote in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        nimet.add(syote)
        print("Uusi nimi.")

    syote = input("Anna nimi: ")

print()
for nimi in nimet:
    print(nimi)

