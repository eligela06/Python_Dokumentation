
class Bankkonto:
    def __init__(self, inhaber, kontostand):
        self.inhaber = inhaber
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        self.kontostand += betrag

konto_elia = Bankkonto("Elia", 1000)
konto_anna = Bankkonto("Anna", 500)

konto_elia.einzahlen(200)

class Auto:
    def __init__(self, inhaber, farbe, marke):
        self.inhaber = inhaber
        self.farbe = farbe
        self.marke = marke

    def fahren(self, sound):
        self.sound = sound
        print(sound)


auto_elia = Auto("Elia", "rot", "Ferrari")
auto_elia.fahren("wrumm")

