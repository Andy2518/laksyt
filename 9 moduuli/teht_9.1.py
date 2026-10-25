class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykynopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

olio = Auto("ABC-123", 142, 0, 0)

print(f"{olio.rekisteritunnus}, {olio.huippunopeus} km/h, {olio.nykynopeus}, {olio.kuljettu_matka}")