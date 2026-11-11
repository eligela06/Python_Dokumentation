def analysiere_zahlen(zahlen):
    """
    Aufgabe 1: Zahlen in einer Liste auswerten.

    `zahlen` ist eine nicht leere Liste von ganzen Zahlen. Gehe die Liste mit
    einer Schleife durch und gib ein Dictionary mit diesen Eintraegen zurueck:

    - "summe": Summe aller Zahlen
    - "minimum": kleinste Zahl
    - "maximum": groesste Zahl
    - "gerade": Anzahl der geraden Zahlen
    - "ungerade": Anzahl der ungeraden Zahlen

    Berechne die Werte selbst mit einer Schleife und verwende fuer diese
    Aufgabe nicht sum(), min() oder max().

    """

    count_even = 0
    count_odd = 0
    summe = 0
    minimum = zahlen[0]
    maximum = zahlen[0]

    for zahl in zahlen:
        summe += zahl
        if zahl % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        if zahl >= maximum:
            maximum = zahl
        if zahl <= minimum:
            minimum = zahl

    result = {
        "summe": summe,
        "minimum": minimum,
        "maximum": maximum,
        "gerade": count_even,
        "ungerade": count_odd
              }
    return result


def filtere_lange_woerter(woerter, mindestlaenge):
    """
    Aufgabe 2: Eine Liste nach der Wortlaenge filtern.

    Gib eine neue Liste mit allen Woertern zurueck, deren Laenge mindestens
    `mindestlaenge` betraegt. Die Reihenfolge muss gleich bleiben. Die
    uebergebene Liste darf nicht veraendert werden.

    Beispiel:
        filtere_lange_woerter(["Hund", "Katze", "Maus"], 5)
        -> ["Katze"]
    """
    words = []
    for word in woerter:
        if len(word) >= mindestlaenge:
            words.append(word)
    return words


def zaehle_woerter(text):
    """
    Aufgabe 3: Woerter in einem Text zaehlen.

    Zerlege den Text an Leerzeichen. Gross- und Kleinschreibung soll keinen
    Unterschied machen. Entferne an jedem Wort am Anfang und Ende die Zeichen
    Punkt, Komma, Ausrufezeichen, Fragezeichen, Semikolon und Doppelpunkt.
    Gib ein Dictionary zurueck, das jedes vorkommende Wort seiner Haeufigkeit
    zuordnet. Bei leerem Text soll ein leeres Dictionary zurueckgegeben werden.

    Beispiel:
        zaehle_woerter("Python macht Spass! Python ist toll.")
        -> {"python": 2, "macht": 1, "spass": 1, "ist": 1, "toll": 1}
    """
    words = list(text.split(" "))
    words_cleaned = []
    cleaned = ""
    for word in words:
        for letter in word:
            if letter not in (".", ",","!","?",";",":"," "):
                letter = letter.lower()
                cleaned += letter
        words_cleaned.append(cleaned)
        cleaned = ""
    if len(text) >= 1:
        result = {wort: words_cleaned.count(wort) for wort in words_cleaned}
    else:
        result = {}

    return result


def finde_besten_schueler(noten):
    """
    Aufgabe 4: Den Schueler mit dem besten Notendurchschnitt finden.

    `noten` ist ein Dictionary mit Schuelernamen als Schluesseln und jeweils
    einer nicht leeren Liste deutscher Schulnoten (ganze Zahlen von 1 bis 6)
    als Wert. Der Schueler mit dem niedrigsten Durchschnitt gewinnt.

    Gib ein Tupel (name, durchschnitt) zurueck. Runde den Durchschnitt auf
    eine Nachkommastelle. Bei Gleichstand gewinnt der Name, der im Dictionary
    zuerst eingetragen wurde. Das Dictionary enthaelt mindestens einen
    Schueler.

    Beispiel:
        finde_besten_schueler({"Mia": [2, 1], "Noah": [2, 2]})
        -> ("Mia", 1.5)
    """

    bester = None
    for schueler in noten:
        if bester == None:
            bester = schueler
            schueler_score = noten.get(schueler)
            notes_schueler = len(schueler_score)
            sum_schueler = sum(schueler_score)
            durchschnitt_schueler = sum_schueler / notes_schueler
            bester_print = (schueler, round(durchschnitt_schueler, 1))
        elif bester != None:
            schueler_score = noten.get(schueler)
            bester_score = noten.get(bester)

            notes_schueler = len(schueler_score)
            sum_schueler = sum(schueler_score)
            durchschnitt_schueler = sum_schueler / notes_schueler

            notes_bester = len(bester_score)
            sum_bester = sum(bester_score)
            durchschnitt_bester = sum_bester / notes_bester

            if durchschnitt_schueler < durchschnitt_bester:
                bester = schueler
                bester_print= (schueler, round(durchschnitt_schueler, 1))

    return bester_print



print(zaehle_woerter("hi   HI"))

x = finde_besten_schueler({"Mia": [2, 1], "Noah": [2, 2], "Elia": [1,1]})
print(x)