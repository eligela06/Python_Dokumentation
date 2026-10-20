# Aufgabe: Schreibe eine rekursive Funktion, die die Fakultät einer Zahl n
# berechnet. Die Fakultät ist n * (n - 1) * ... * 1; für n <= 1 ist sie 1.
def fakultaet(n):    
    if n <= 1:        
        return 1    
    return n * fakultaet(n - 1)