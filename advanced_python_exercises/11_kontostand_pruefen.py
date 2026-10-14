"""Übung 11: Abheben mit Kontostand-Prüfung

Schreibe eine Funktion `abheben(kontostand, betrag)`.

- Wenn genug Geld auf dem Konto ist, gib den neuen Kontostand zurück.
- Wenn nicht genug Geld da ist, gib den alten Kontostand zurück und zeige
  eine Meldung an.
- Ein Betrag kleiner oder gleich 0 soll abgelehnt werden.

Teste die Funktion mit einem erfolgreichen und einem abgelehnten Versuch.
"""


def abheben(kontostand, betrag):
    # TODO: Prüfe zuerst, ob betrag positiv ist.
    if betrag <= 0:
        print("gib einen gültigen betrag ein")
    # TODO: Prüfe danach, ob genug Geld auf dem Konto ist.
    elif kontostand >= betrag:
        print("du hast genug geld")
        kontostand -= betrag
    else:
        print("kontostand zu niedrig")
    # TODO: Gib den passenden Kontostand zurück.
    return kontostand



print(abheben(25, 10))
print(abheben(25, 40))
