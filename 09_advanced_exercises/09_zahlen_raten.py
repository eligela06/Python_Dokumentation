"""Übung 9: Kleines Ratespiel

Lege eine geheime Zahl fest. Frage den Benutzer so lange nach einer Zahl,
bis er richtig geraten hat. Sage nach jedem Versuch, ob die geheime Zahl
größer oder kleiner ist.
"""

geheime_zahl = 7

# TODO: Wiederhole die Eingabe in einer while-Schleife.
# TODO: Wandle die Eingabe mit int() in eine Zahl um.
# TODO: Gib einen passenden Hinweis oder eine Glückwunschmeldung aus.

while True:
    zahl = int(input("Gib zahl ein: "))
    if zahl == geheime_zahl:
        print("du hast gewonnen")
        break
    elif zahl < geheime_zahl:
        print("zahl ist grösser")
    else:
        print("zahl ist kleiner")