# Aufgabe: Schreibe eine rekursive Funktion, die prüft, ob eine Zeichenkette
# ein Palindrom ist. Ein Palindrom liest sich vorwärts und rückwärts gleich.
def ist_palindrom(s):    
    if len(s) <= 1:        
        return True    
    if s[0] != s[-1]:        
        return False    
    return ist_palindrom(s[1:-1])