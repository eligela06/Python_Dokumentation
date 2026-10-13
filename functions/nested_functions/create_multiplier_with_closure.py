def multiplizierer(faktor):
    def multipliziere(zahl):
        return zahl * faktor  # Zugriff auf 'faktor' der äußeren Funktion
    return multipliziere

verdoppeln = multiplizierer(2)
print(verdoppeln(5))  # Ausgabe: 10
