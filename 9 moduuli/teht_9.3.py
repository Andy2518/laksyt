class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykynopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos_kmh):
        uusi_nopeus = self.nykynopeus + nopeuden_muutos_kmh

        if uusi_nopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus

        elif uusi_nopeus < 0:
            self.nykynopeus = 0

        else:
            self.nykynopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        kasvu = self.nykynopeus * tuntimaara
        self.kuljettu_matka = self.kuljettu_matka + kasvu

olio = Auto("ABC-123", 142, 0, 0)

olio.kiihdyta(30)
olio.kiihdyta(70)
olio.kiihdyta(50)

print(f"Auton kiihtyvyys on: {olio.nykynopeus} km/h")

olio.kiihdyta(-200)

print(f"Auton hätäjarrutus on: {olio.nykynopeus} km/h")

olio.kuljettu_matka = 2000
olio.nykynopeus = 60

olio.kulje(1.5)

print(f"Auton kuljettu matka on: {olio.kuljettu_matka} km")