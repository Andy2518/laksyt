class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

olio = Auto("ABC-123", 142)

print(olio.rekisteritunnus)
print(olio.huippunopeus)
print(olio.nykynopeus)
print(olio.kuljettu_matka)