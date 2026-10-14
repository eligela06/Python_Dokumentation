"""Übung 2: Zahlen aus einer Liste auswählen

Gehe mit einer for-Schleife durch die Liste und sammle alle geraden Zahlen
in einer neuen Liste. Gib die neue Liste aus.
"""

zahlen = [3, 8, 12, 5, 7, 20]
gerade_zahlen = [num for num in zahlen if num % 2 == 0]


print(gerade_zahlen)
