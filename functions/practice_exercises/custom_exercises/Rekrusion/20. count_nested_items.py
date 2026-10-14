# Aufgabe: Schreibe eine Funktion count_items(data), die zählt, wie viele
# Elemente (keine Listen) in einer verschachtelten Liste stecken.
# Die Funktion muss sich selbst aufrufen, wenn ein Element wieder eine Liste ist.
# Beispiel: count_items(["a", ["b", "c"], [["d"], "e"]]) gibt 5 zurück.

items = 0
def count_items(data):
    global items
    for element in data:
        if type(element) == list:
            count_items(element)
        else:
            items += 1
    return items
print(count_items(["a", ["b", "c"], [["d"], "e",[], "e"]]))