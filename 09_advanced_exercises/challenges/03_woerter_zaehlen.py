"""Übung 3: Wörter zählen

Schreibe eine Funktion, die ein Wort und eine Wortliste erhält und zählt,
wie oft das Wort vorkommt. Groß- und Kleinschreibung soll egal sein.
"""

woerter = ["Python", "lernen", "macht", "Spaß", "python", "macht"]


def zaehle_wort(suchwort, liste):
    count = 0
    for wort in liste:
        if wort.lower() == suchwort.lower():
            count += 1
    return count


print(zaehle_wort("python", woerter))  # Erwartet: 2
