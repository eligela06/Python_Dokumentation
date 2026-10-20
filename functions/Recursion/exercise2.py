# Aufgabe: Schreibe eine rekursive Funktion, die die Zahlen in einer Liste
# addiert. Für eine leere Liste soll die Summe 0 sein.
def summe(liste):    
    if not liste:        
        return 0    
    return liste[0] + summe(liste[1:])