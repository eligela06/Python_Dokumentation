import random
banknummern = []
class Bankkonto:
    def __init__(self, inhaber,kontostand, username):
        self.inhaber = inhaber
        self.banknummer = f"CH{(random.randint(0,10001))}"
        while True:
            if self.banknummer not in banknummern:
                banknummern.append(self.banknummer)
                break
            else:
                self.banknummer = f"CH{(random.randint(0,10001))}"

        self.kontostand = kontostand
        self.username = username
        

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def abheben(self, betrag):
        self.kontostand -= betrag
    @property
    def datenausgeben(self):
        print(f"Inhaber: {self.inhaber}")
        print(f"Banknummer: {self.banknummer}")
        print(f"Kontostand: {self.kontostand}")

elia_konto = Bankkonto("Elia", 200, "elia")

lenny_konto = Bankkonto("Lenny", 5, "lenny")

max_konto = Bankkonto("Max", 1200, "max")

dimo_konto = Bankkonto("Dimo", 60, "dimo")

lenny_konto.datenausgeben