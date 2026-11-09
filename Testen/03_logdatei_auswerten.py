"""
Praxisaufgabe: Logauswertung reparieren und erweitern

Ein Programm bekommt Logzeilen aus einem Server. Der vorhandene Auswerter
funktioniert noch nicht in allen Faellen und soll verbessert werden.

Format einer gueltigen Zeile:
    ZEITSTEMPEL LEVEL NACHRICHT

Aufgabe A - `werte_logs_aus(logzeilen)` reparieren:
- Erlaubte Level sind DEBUG, INFO, WARNING und ERROR.
- Die Nachricht kann mehrere Woerter enthalten.
- Eine gueltige Zeile hat einen Zeitstempel, ein bekanntes Level und eine
  nicht leere Nachricht.
- Zaehle alle gueltigen Zeilen insgesamt und pro Level. Das Ergebnis soll
  auch Level mit Anzahl null enthalten.
- Sammle vollstaendige Originalzeilen mit Level ERROR in `fehler`.
- Sammle ungueltige Originalzeilen in `ungueltig`.
- Erhalte in beiden Listen die urspruengliche Reihenfolge.
- Gib ein Dictionary mit `gesamt`, `level`, `fehler` und `ungueltig` zurueck.

Aufgabe B - `filtere_fehler(auswertung, stichwort)` ergaenzen:
- Durchsuche nur die Fehlerliste aus der Auswertung.
- Gib Originalzeilen zurueck, die das Stichwort enthalten.
- Die Suche soll Gross-/Kleinschreibung ignorieren.
- Die Reihenfolge soll erhalten bleiben.

Beispiel:
    zeilen = [
        "2026-11-09T08:30:00 INFO Dienst gestartet",
        "2026-11-09T08:31:00 ERROR Verbindung fehlgeschlagen",
        "ungueltige Zeile",
        "2026-11-09T08:32:00 ERROR Verbindung erneut fehlgeschlagen",
    ]
    auswertung = werte_logs_aus(zeilen)
    filtere_fehler(auswertung, "VERBINDUNG")
    -> [
        "2026-11-09T08:31:00 ERROR Verbindung fehlgeschlagen",
        "2026-11-09T08:32:00 ERROR Verbindung erneut fehlgeschlagen",
    ]

Weitere Tests:
- Leere Eingabe.
- Unbekanntes Level.
- Zeile ohne Nachricht.
- Eine Nachricht mit mehreren Woertern und einem Stichwort in anderer
  Gross-/Kleinschreibung.
"""


def werte_logs_aus(logzeilen):
    level_anzahl = {"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0}
    fehler = []
    ungueltig = []
    gesamt = 0

    for zeile in logzeilen:
        teile = zeile.split()
        if len(teile) < 3:
            ungueltig.append(zeile)
            continue

        zeitstempel = teile[0]
        level = teile[1]
        nachricht = teile[2]
        level_anzahl[level] += 1
        gesamt += 1

        if level == "ERROR":
            fehler.append(zeile)

    return {
        "gesamt": gesamt,
        "level": level_anzahl,
        "fehler": fehler,
        "ungueltig": ungueltig,
    }


def filtere_fehler(auswertung, stichwort):
    pass


if __name__ == "__main__":
    logzeilen = [
        "2026-11-09T08:30:00 INFO Dienst gestartet",
        "2026-11-09T08:31:00 ERROR Verbindung fehlgeschlagen",
        "ungueltige Zeile",
        "2026-11-09T08:32:00 ERROR Verbindung erneut fehlgeschlagen",
    ]
    auswertung = werte_logs_aus(logzeilen)
    print("Auswertung:", auswertung)
    print("Gefilterte Fehler:", filtere_fehler(auswertung, "VERBINDUNG"))
