class Bankkonto:
    def __init__(self, inhaber, banknummer, kontostand, username):
        self.inhaber = inhaber
        self.banknummer = banknummer
        self.kontostand = kontostand
        self.username = username

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def abheben(self, betrag):
        self.kontostand -= betrag

    def datenausgeben(self):
        print(f"Inhaber: {self.inhaber}")
        print(f"Banknummer: {self.banknummer}")
        print(f"Kontostand: {self.kontostand}")

elia_konto = Bankkonto("Elia", "CH45434565", 200, "elia")

lenny_konto = Bankkonto("Lenny", "DE8765432", 5, "lenny")

max_konto = Bankkonto("Max","CH12345687", 1200, "max")

dimo_konto = Bankkonto("Dimo","CH765432", 60, "dimo")