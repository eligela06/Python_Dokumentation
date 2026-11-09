"""
Praxisaufgabe: Bestellverarbeitung reparieren und erweitern

Ein Shop verarbeitet Bestellungen mit mehreren Positionen. Der bestehende
Code hat Fehler und muss vor dem Einsatz repariert werden.

Aufgabe A - `verarbeite_bestellung(lager, bestellung)` reparieren:
- Jeder Bestellposten ist ein Tupel `(artikel, menge)`.
- Artikel koennen mehrfach in einer Bestellung vorkommen.
- Pruefe, ob die Gesamtmenge jedes Artikels verfuegbar ist.
- Ist ein Artikel unbekannt oder nicht ausreichend auf Lager, lehne die
  gesamte Bestellung ab und liefere `(False, lager_kopie)` zurueck.
- Bei erfolgreicher Bestellung liefere `(True, neuer_lagerbestand)` zurueck.
- Veraendere das uebergebene `lager` niemals, weder bei Erfolg noch bei
  Ablehnung.

Aufgabe B - `fasse_bestellung_zusammen(bestellung)` ergaenzen:
- Gib ein Dictionary mit der Gesamtmenge pro Artikel zurueck.
- Die Reihenfolge der Artikel soll der ersten Nennung in der Bestellung
  entsprechen.

Beispiel:
    lager = {"Laptop": 3, "Maus": 5}
    bestellung = [("Maus", 2), ("Laptop", 1), ("Maus", 1)]
    fasse_bestellung_zusammen(bestellung)
    -> {"Maus": 3, "Laptop": 1}
    verarbeite_bestellung(lager, bestellung)
    -> (True, {"Laptop": 2, "Maus": 2})

Weitere Tests:
- Eine Bestellung mit unbekanntem Artikel.
- Mehrere Positionen, deren Summe den Lagerbestand uebersteigt.
- Eine Bestellung, die einen Artikelbestand genau auf null bringt.
- Pruefe nach jedem Aufruf, dass das urspruengliche `lager` unveraendert ist.
"""


def verarbeite_bestellung(lager, bestellung):
    neuer_lagerbestand = lager

    for artikel, menge in bestellung:
        if artikel not in neuer_lagerbestand:
            return False, neuer_lagerbestand
        if neuer_lagerbestand[artikel] < menge:
            return False, neuer_lagerbestand
        neuer_lagerbestand[artikel] -= menge

    return True, neuer_lagerbestand


def fasse_bestellung_zusammen(bestellung):
    pass


if __name__ == "__main__":
    lager = {"Laptop": 3, "Maus": 5}
    bestellung = [("Maus", 2), ("Laptop", 1), ("Maus", 1)]
    print("Zusammenfassung:", fasse_bestellung_zusammen(bestellung))
    print("Bestellung:", verarbeite_bestellung(lager, bestellung))
    print("Urspruengliches Lager:", lager)
