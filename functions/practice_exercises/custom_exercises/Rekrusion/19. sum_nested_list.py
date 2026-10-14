# Aufgabe: Schreibe eine Funktion sum_nested(data), die alle Zahlen in einer
# verschachtelten Liste addiert. Die Funktion muss sich selbst aufrufen,
# wenn ein Element wieder eine Liste ist.
# Beispiel: sum_nested([1, [2, 3], [4, [5]]]) gibt 15 zurück.
sum = 0
def sum_nested(data):
    global sum
    for element in data:
        if type(element) == list:
            sum_nested(element)
        else:
            sum += element
    return sum

print(sum_nested([1, [2, 3], [4, [3]], 2,[1]]))