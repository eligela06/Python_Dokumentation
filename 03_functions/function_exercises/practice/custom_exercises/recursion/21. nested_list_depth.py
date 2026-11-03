# Aufgabe: Schreibe eine Funktion depth(data), die angibt, wie tief eine Liste
# verschachtelt ist. Die Funktion muss sich selbst aufrufen,
# wenn ein Element wieder eine Liste ist.
# Beispiel: depth([1, 2]) gibt 1 zurück, depth([1, [2, [3]]]) gibt 3 zurück.

def depth(data):
    nested_depths = [
        depth(element)
        for element in data
        if isinstance(element, list)
    ]
    return 1 + max(nested_depths, default=0)


print(depth([1, [2, [3]], [1]]))
