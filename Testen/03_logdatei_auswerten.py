"""
Praxisaufgabe 3: Logdatei auswerten

Ein Programm schreibt eine Logzeile pro Ereignis. Eine Zeile hat dieses Format:

    ZEITSTEMPEL LEVEL NACHRICHT

Zum Beispiel:

    2026-11-09T08:30:00 INFO Dienst gestartet

Implementiere `werte_logs_aus(logzeilen)`.

Anforderungen:
- Teile jede Zeile an Leerraum in maximal drei Teile: Zeitstempel, Level und
  Nachricht. Die Nachricht darf weitere Leerzeichen enthalten.
- Erkenne die Level `DEBUG`, `INFO`, `WARNING` und `ERROR`.
- Eine Zeile ist gueltig, wenn sie genau diese drei nicht leeren Teile hat
  und das Level bekannt ist.
- Zaehle die gueltigen Zeilen insgesamt und pro Level. Das Ergebnis soll alle
  vier Level enthalten, auch wenn ihre Anzahl null ist.
- Sammle vollstaendige Originalzeilen mit dem Level `ERROR` in einer Liste.
  Behalte dabei die urspruengliche Reihenfolge.
- Sammle alle ungueltigen Originalzeilen ebenfalls in einer Liste und behalte
  ihre Reihenfolge.
- Gib ein Dictionary mit den Schluesseln `gesamt`, `level`, `fehler` und
  `ungueltig` zurueck. `gesamt` zaehlt nur gueltige Zeilen.

Beispiel:
    zeilen = [
        "2026-11-09T08:30:00 INFO Dienst gestartet",
        "2026-11-09T08:31:00 ERROR Verbindung fehlgeschlagen",
        "keine gueltige Logzeile",
        "2026-11-09T08:32:00 ERROR Erneuter Verbindungsversuch fehlgeschlagen",
    ]
    werte_logs_aus(zeilen)
    -> {
        "gesamt": 3,
        "level": {"DEBUG": 0, "INFO": 1, "WARNING": 0, "ERROR": 2},
        "fehler": [
            "2026-11-09T08:31:00 ERROR Verbindung fehlgeschlagen",
            "2026-11-09T08:32:00 ERROR Erneuter Verbindungsversuch fehlgeschlagen",
        ],
        "ungueltig": ["keine gueltige Logzeile"],
    }

Teste zusaetzlich eine leere Eingabe, ein unbekanntes Level und eine Zeile
ohne Nachricht.
"""


def werte_logs_aus(logzeilen):
    pass
