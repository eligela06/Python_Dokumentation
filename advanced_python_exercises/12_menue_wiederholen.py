"""Übung 12: Menü wiederholen

Erweitere die Menü-Aufgabe: Zeige das Menü so lange, bis der Benutzer
"ende" eingibt.

- Bei "hallo" rufst du `begruesse()` auf.
- Bei "tschüss" rufst du `verabschiede()` auf.
- Bei einer anderen Eingabe zeigst du eine Fehlermeldung.
- Groß-/Kleinschreibung soll egal sein.

Tipp: Verwende `while`, `input()`, `.lower()` und `break`.
"""


def begruesse():
    print("Hallo!")


def verabschiede():
    print("Auf Wiedersehen!")


# TODO: Schreibe eine while-Schleife und rufe die Funktionen passend auf.
while True:
    auswahl = input("gib etwas ein: ").lower()
    if auswahl == 'ende':
        break
    elif auswahl == 'hallo':
        begruesse()
    elif auswahl == 'tschüss':
        verabschiede()
    else: 
        print("ungültige ausgabe")