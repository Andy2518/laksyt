def luku(kokonaisluku):
    summa = 0
    for luvut in kokonaisluku:
        summa += luvut
    return summa

lista = [10, 20, 70]
vastaus = luku(lista)
print(vastaus)