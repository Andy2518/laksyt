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

    def kiihdyta(self, nopeuden_muutos_kmh):
        self.nykynopeus += nopeuden_muutos_kmh

        if self.nykynopeus > 0:
            self.nykynopeus = 0

        elif self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus

olio = Auto("ABC-123", 142)

olio.kiihdyta(30)
olio.kiihdyta(70)
olio.kiihdyta(50)
olio.tietojentulostus()
olio.kiihdyta(-200)
olio.tietojentulostus()




