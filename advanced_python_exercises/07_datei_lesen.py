"""Übung 7: Text aus einer Datei lesen

Erstelle im selben Ordner eine Datei `notiz.txt` mit einem Satz.
Öffne sie mit `with open(...)` und gib ihren Inhalt aus.
Tipp: Verwende encoding="utf-8".
"""

from pathlib import Path

datei_pfad = Path(__file__).with_name("notiz.txt")

with open(datei_pfad, "r", encoding="utf-8") as datei:
    inhalt = datei.read()

print(inhalt)
