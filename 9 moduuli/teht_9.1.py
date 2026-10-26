class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

    def tietojentulostus(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Nykynopeus: {self.nykynopeus}")
        print(f"Kuljettu matka: {self.kuljettu_matka}")

olio = Auto("ABC-123", 142)

olio.tietojentulostus()