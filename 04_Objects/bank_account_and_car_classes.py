class Bankkonto:
    def __init__(self, kontostand=0):
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        if betrag <= 0:
            print("Der Betrag muss positiv sein.")
            return

        self.kontostand += betrag


class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.bankkonto = Bankkonto()
        self.auto = None
        

class Auto:
    def __init__(self, inhaber, farbe, marke):
        self.inhaber = inhaber
        self.farbe = farbe
        self.marke = marke

    def fahren(self, sound):
        self.sound = sound
        print(sound)



person1 = Person("Elia Bischof", 15)
person1.bankkonto.einzahlen(100)
print(f"{person1.name} hat {person1.bankkonto.kontostand} Euro auf dem Konto.")

person1.auto = Auto(person1, "blau", "Beispielmarke")
person1.auto.fahren("Brumm")
