"""Übung 13: Rechteck um Umfang erweitern

Schreibe eine Klasse `Rechteck` mit `breite` und `hoehe`.

- Die Methode `flaeche()` gibt Breite mal Höhe zurück.
- Die Methode `umfang()` gibt 2 mal (Breite plus Höhe) zurück.
- Speichere die Ergebnisse nicht in Attributen mit denselben Namen wie
  deine Methoden.

Teste dein Rechteck mit Breite 4 und Höhe 3.
Erwartete Fläche: 12. Erwarteter Umfang: 14.
Rufe beide Methoden jeweils zweimal auf.
"""


class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe


    def flaeche(self):
        # TODO: Berechne und gib die Fläche zurück.
        return self.breite * self.hoehe


    def umfang(self):
        # TODO: Berechne und gib den Umfang zurück.
        return (2*self.hoehe)+(2*self.breite)
        pass


# TODO: Erzeuge ein Rechteck und teste beide Methoden zweimal.

rechteck = Rechteck(4,3)
print(rechteck.flaeche())
print(rechteck.umfang())
