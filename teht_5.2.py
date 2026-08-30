lista = []

while True:
    syote = input("Anna syote: ")

    if syote == "":
        break

    kokonaisluku = int(syote)
    lista.append(kokonaisluku)
    lista.sort(reverse=True)

print(lista[:5])

for luku in lista[:5]:
    print(luku)











