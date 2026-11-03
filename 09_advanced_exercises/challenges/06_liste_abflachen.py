"""Übung 6: Eine einfache verschachtelte Liste abflachen

Die Liste enthält Zahlen und Unterlisten mit Zahlen. Erstelle mit zwei
for-Schleifen eine neue Liste, in der alle Zahlen der Reihe nach stehen.
Die Unterlisten sind hier nur eine Ebene tief.
"""

verschachtelt = [1, [2, 3], 4, [5, 6]]
flach = []

for element in verschachtelt:
    if isinstance(element, list):
        for zahl in element:
            flach.append(zahl)
    else:
        flach.append(element)

print(flach)  # Erwartet: [1, 2, 3, 4, 5, 6]
