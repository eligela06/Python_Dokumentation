"""
Praxisaufgabe 2: Lagerbestand und Bestellung verwalten

Ein kleines Geschaeft nimmt eine Bestellung mit mehreren Positionen entgegen.
Bevor die Bestellung verarbeitet wird, muss geprueft werden, ob alle Artikel
im Lager vorhanden sind und die bestellte Menge verfuegbar ist.

Implementiere `verarbeite_bestellung(lager, bestellung)`.

Eingaben:
- `lager`: Dictionary aus Artikelname und verfuegbarer Menge
- `bestellung`: Liste von `(artikel, menge)`-Tupeln
- Artikel und Mengen sind Strings beziehungsweise positive ganze Zahlen.
  Ein Artikel darf in der Bestellung mehrmals vorkommen.

Anforderungen:
- Addiere mehrere Positionen desselben Artikels, bevor du den Lagerbestand
  pruefst.
- Ist ein Artikel unbekannt oder die Gesamtmenge nicht verfuegbar, lehne die
  ganze Bestellung ab. Gib dann `(False, lager_kopie)` zurueck; der uebergebene
  Lagerbestand darf nicht veraendert werden.
- Wenn alle Positionen erfuellbar sind, ziehe die bestellten Mengen ab und
  gib `(True, neuer_lagerbestand)` zurueck.
- Veraendere das uebergebene Dictionary auch bei einer erfolgreichen
  Bestellung nicht direkt, sondern liefere ein neues Dictionary.

Beispiel:
    lager = {"Laptop": 3, "Maus": 5}
    bestellung = [("Maus", 2), ("Laptop", 1), ("Maus", 1)]
    verarbeite_bestellung(lager, bestellung)
    -> (True, {"Laptop": 2, "Maus": 2})
    # `lager` ist danach weiterhin {"Laptop": 3, "Maus": 5}.

Beispiel fuer eine abgelehnte Bestellung:
    verarbeite_bestellung(
        {"Laptop": 3, "Maus": 5},
        [("Laptop", 1), ("Maus", 6)],
    )
    -> (False, {"Laptop": 3, "Maus": 5})

Teste zusaetzlich eine Bestellung mit einem unbekannten Artikel und eine
Bestellung, die den Lagerbestand genau auf null bringt.
"""


def verarbeite_bestellung(lager, bestellung):
    pass
