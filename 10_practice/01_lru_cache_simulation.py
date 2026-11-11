"""
Praxisaufgabe: LRU-Cache reparieren und erweitern

Du uebernimmst einen kleinen Cache, der in einem Projekt verwendet werden
soll. Die erste Version ist bereits programmiert, hat aber noch Fehler.
Untersuche den Code, korrigiere ihn und ergaenze die angekuendigte Funktion.

Der Cache speichert Eintraege in einer Liste:
- vorne steht der am laengsten nicht verwendete Eintrag
- hinten steht der zuletzt verwendete Eintrag

Aufgabe A - vorhandenen Code reparieren:
- `get` liefert den gespeicherten Wert oder `None`, wenn der Schluessel fehlt.
- Ein erfolgreicher `get` macht den Eintrag zum zuletzt verwendeten.
- `put` speichert einen neuen Eintrag oder aktualisiert einen vorhandenen.
  Ein aktualisierter Eintrag gilt danach als zuletzt verwendet.
- Ist der Cache voll und kommt ein neuer Schluessel dazu, wird der am
  laengsten nicht verwendete Eintrag entfernt.
- Ein fehlgeschlagener `get` veraendert die Reihenfolge nicht.

Aufgabe B - Funktion ergaenzen:
- Implementiere `berechne_trefferquote(statistik)`.
- Die Funktion bekommt das Statistik-Dictionary aus `simuliere_cache`.
- Sie gibt die Trefferquote in Prozent zurueck, auf eine Nachkommastelle
  gerundet.
- Gibt es keine `get`-Aufrufe, soll die Funktion `0.0` zurueckgeben.

Schnittstellen:
- `simuliere_cache(kapazitaet, operationen)` gibt
  `(ergebnisse, cache_eintraege, statistik)` zurueck.
- `ergebnisse` enthaelt die Ergebnisse aller `get`-Aufrufe.
- `cache_eintraege` ist die finale Liste von `(schluessel, wert)`-Tupeln.
- `statistik` enthaelt `treffer` und `fehlversuche` fuer `get`-Aufrufe.
- `berechne_trefferquote(statistik)` gibt einen Prozentwert zwischen 0.0 und
  100.0 zurueck.

Beispiel fuer den Cache:
    operationen = [
        ("put", "A", 1),
        ("put", "B", 2),
        ("get", "A"),
        ("put", "C", 3),
        ("get", "B"),
        ("get", "A"),
    ]

Erwartetes Ergebnis nach der Reparatur:
    (
        [1, None, 1],
        [("C", 3), ("A", 1)],
        {"treffer": 2, "fehlversuche": 1},
    )
    berechne_trefferquote({"treffer": 2, "fehlversuche": 1}) -> 66.7

Teste auch selbst:
- Kapazitaet 1.
- Einen vorhandenen Schluessel aktualisieren.
- Mehrere get-Aufrufe auf denselben Eintrag.
- Einen fehlgeschlagenen get.
- Keine get-Aufrufe (Trefferquote 0.0).
"""


def simuliere_cache(kapazitaet, operationen):
    cache = []
    ergebnisse = []
    treffer = 0
    fehlversuche = 0

    for operation in operationen:
        aktion = operation[0]
        schluessel = operation[1]

        if aktion == "get":
            gefunden = False
            for cache_schluessel, wert in cache:
                if cache_schluessel == schluessel:
                    ergebnisse.append(wert)
                    treffer += 1
                    gefunden = True
                    break
            if not gefunden:
                ergebnisse.append(None)
                fehlversuche += 1

        elif aktion == "put":
            wert = operation[2]
            gefunden = False
            for index, (cache_schluessel, alter_wert) in enumerate(cache):
                if cache_schluessel == schluessel:
                    cache[index] = (schluessel, wert)
                    gefunden = True
                    break

            if not gefunden:
                if len(cache) >= kapazitaet:
                    cache.pop()
                cache.append((schluessel, wert))

    statistik = {"treffer": treffer, "fehlversuche": fehlversuche}
    return ergebnisse, cache, statistik


def berechne_trefferquote(statistik):
    pass


if __name__ == "__main__":
    operationen = [
        ("put", "A", 1),
        ("put", "B", 2),
        ("get", "A"),
        ("put", "C", 3),
        ("get", "B"),
        ("get", "A"),
    ]

    ergebnisse, cache, statistik = simuliere_cache(2, operationen)
    print("Ergebnisse:", ergebnisse)
    print("Cache:", cache)
    print("Statistik:", statistik)
    print("Trefferquote:", berechne_trefferquote(statistik), "%")
