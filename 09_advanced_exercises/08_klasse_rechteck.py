"""Übung 8: Eine einfache Klasse schreiben

Erstelle eine Klasse `Rechteck` mit den Attributen breite und hoehe.
Schreibe eine Methode `flaeche()`, die breite mal hoehe zurückgibt.
Erzeuge ein Rechteck und gib seine Fläche aus.
"""


class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe
        

    def flaeche(self):
        self.flaeche = self.hoehe * self.breite
        return self.flaeche



rechteck = Rechteck(4, 4)
print(rechteck.flaeche())  # Erwartet: 12
