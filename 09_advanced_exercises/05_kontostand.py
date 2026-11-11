"""Übung 5: Kontostand mit Funktionen ändern

Schreibe `einzahlen(kontostand, betrag)`, die den neuen Kontostand zurückgibt.
Schreibe danach `abheben(kontostand, betrag)`. Abheben soll nur erlaubt sein,
wenn genug Geld auf dem Konto ist. Gib den Kontostand nach jeder Änderung aus.
"""


def einzahlen(kontostand, betrag):
    kontostand += betrag
    return kontostand


def abheben(kontostand, betrag):
    kontostand -= betrag
    return kontostand


kontostand = 20
kontostand = einzahlen(kontostand, 10)
kontostand = abheben(kontostand, 5)
print(kontostand)
