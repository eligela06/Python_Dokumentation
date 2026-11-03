"""Übung 15: Zeilen in einer Datei zählen

Öffne die Datei `notiz.txt` aus diesem Ordner und zähle, wie viele Zeilen
sie enthält.

- Verwende `with open(...)` und `encoding="utf-8"`.
- Verwende eine for-Schleife, um die Zeilen zu zählen.
- Fange `FileNotFoundError` ab und gib eine hilfreiche Meldung aus.

Tipp: Verwende `Path(__file__).with_name("notiz.txt")`, damit die Datei
unabhängig vom aktuellen Arbeitsordner gefunden wird.
"""

from pathlib import Path

datei_pfad = Path(__file__).with_name("notiz.txt")

# TODO: Öffne die Datei in einem with-Block.
# TODO: Zähle die Zeilen mit einer for-Schleife.
# TODO: Behandle den Fall, dass die Datei nicht existiert.
