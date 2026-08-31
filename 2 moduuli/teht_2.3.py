# Annetaan syöte kanta ja korkeudelle.
kanta = float(input("Suorakulmion kanta:"))
korkeus = float(input("Suorakulmion korkeus:"))

# Lasketaan piiri ja pinta-ala edellisen rivien muuttujilla.
p = 2 * (kanta + korkeus)
A = kanta * korkeus

# Tulostetaan piiri ja pinta-ala p ja A muuttujilla.
print(f"Suorakolmion piiri on {p}")
print(f"Suorakulmion pinta-ala on {A}")
