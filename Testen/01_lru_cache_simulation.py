"""
Praxisaufgabe 1: LRU-Cache simulieren

Ein Cache speichert haeufig benoetigte Werte, damit sie schneller verfuegbar
sind. Der Cache hat eine feste Kapazitaet. Ist er voll, wird beim Speichern
eines neuen Schluessels der am laengsten nicht verwendete Eintrag entfernt
(Least Recently Used, kurz LRU).

Implementiere `simuliere_cache(kapazitaet, operationen)`.

Eingaben:
- `kapazitaet`: positive ganze Zahl
- `operationen`: Liste von Tupeln
  - `("put", schluessel, wert)` speichert oder aktualisiert einen Wert
  - `("get", schluessel)` liest einen Wert aus dem Cache

Anforderungen:
- Der Cache startet leer.
- Ein erfolgreicher `get` macht den Eintrag zum zuletzt verwendeten.
- Ein `get` fuer einen fehlenden Schluessel liefert `None` und veraendert die
  Reihenfolge nicht.
- Ein `put` fuer einen schon vorhandenen Schluessel aktualisiert den Wert und
  macht den Eintrag zum zuletzt verwendeten.
- Bei einem neuen `put` in einem vollen Cache wird der am laengsten nicht
  verwendete Eintrag entfernt.
- Gib ein Tupel `(ergebnisse, cache_eintraege)` zurueck. `ergebnisse` enthaelt
  die Rueckgabewerte aller `get`-Operationen in ihrer Reihenfolge.
  `cache_eintraege` ist eine Liste von `(schluessel, wert)`-Tupeln, geordnet
  vom am laengsten nicht verwendeten bis zum zuletzt verwendeten Eintrag.
- Verwende fuer diese Aufgabe keine fertige Cache-Klasse oder `OrderedDict`.

Beispiel:
    operationen = [
        ("put", "A", 1),
        ("put", "B", 2),
        ("get", "A"),
        ("put", "C", 3),
        ("get", "B"),
        ("get", "A"),
    ]
    simuliere_cache(2, operationen)
    -> ([1, None, 1], [("C", 3), ("A", 1)])

Teste zusaetzlich:
- Ein Cache mit Kapazitaet 1.
- Das Aktualisieren eines vorhandenen Schluessels.
- Mehrere `get`-Operationen auf denselben Eintrag.
"""


def simuliere_cache(kapazitaet, operationen):
    pass
