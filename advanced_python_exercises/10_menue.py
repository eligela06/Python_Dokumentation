"""Übung 10: Einfaches Menü mit Funktionen

Schreibe zwei Funktionen: `begruesse()` und `verabschiede()`.
Rufe je nach Auswahl die passende Funktion auf.
Erweitere das Menü anschließend um eine weitere Auswahl.
"""


def begruesse():
    print("Hallo!")


def verabschiede():
    print("Auf Wiedersehen!")


auswahl = input("Gib 'hallo' oder 'tschüss' ein: ")

if auswahl == 'hallo':
    begruesse()
elif auswahl not in ('hallo','tschüss'):
    print("Fehler")
else:
    verabschiede()
