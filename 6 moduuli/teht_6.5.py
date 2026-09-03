def luvut(kokonaisluku):
    karsittu_lista = []
    for luku in kokonaisluku:
        if luku % 2 == 0:
            karsittu_lista.append(luku)
    return karsittu_lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vastaus = luvut(lista)
print(lista)
print(vastaus)

