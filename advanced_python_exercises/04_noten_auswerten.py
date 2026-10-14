"""Übung 4: Noten auswerten

Berechne den Durchschnitt der Noten in der Liste und gib die beste Note aus.
Verwende sum() und len() für den Durchschnitt.
"""

noten = [4, 5, 3, 6, 5]

durchschnitt = sum(noten) / len(noten)
best = max(noten)
print(durchschnitt, best)
