class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tietojentulostus(self):
        print(f"Nimi: {self.nimi}")


class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tietojentulostus(self):
        super().tietojentulostus()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")


class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tietojentulostus(self):
        super().tietojentulostus()
        print(f"Päätoimittaja: {self.päätoimittaja}")


lehti = Lehti("Aku-Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tietojentulostus()
kirja.tietojentulostus()


