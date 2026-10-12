total = 0


def add_to_total(current_total, x):
    return current_total + x


total = add_to_total(total, 5)
print(f"Nach der Parameter-Variante: total = {total}")


def add_to_total_global(x):
    global total
    total = total + x


add_to_total_global(5)
print(f"Nach der global-Variante: total = {total}")
print(f"Endgültiger Wert von total: {total}")

# - Ohne global behandelt Python total bei einer Zuweisung als lokale Variable.
# - Die ursprüngliche Funktion las diese lokale Variable vor ihrer Initialisierung: UnboundLocalError.
# - Die Parameter-Variante übergibt den Wert sichtbar und gibt den neuen Wert zurück.
# - global ändert die globale Variable direkt; das ist bequemer, aber die Abhängigkeit ist weniger sichtbar.
