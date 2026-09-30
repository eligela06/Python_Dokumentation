game_loop = True

while game_loop:
    try:
        calc = (input("Schreibe deine Rechnung auf (press 'x' for exit): ")).strip().lower()

        operator_plus = calc.find("+")
        operator_minus = calc.find("-")
        operator_mult = calc.find("*")
        operator_div = calc.find("/")

        if calc == "x":
            break

        elif operator_plus != -1:
            number1 = int(calc[0:operator_plus])
            number2 = int(calc[operator_plus + 1:])
            result = number1 + number2
            print(result)

        elif operator_minus != -1:
            number1 = int(calc[0:operator_minus])
            number2 = int(calc[operator_minus + 1:])
            result = number1 - number2
            print(result)

        elif operator_mult != -1:
            number1 = int(calc[0:operator_mult])
            number2 = int(calc[operator_mult + 1:])
            result = number1 * number2
            print(result)

        elif operator_div != -1:
            number1 = int(calc[0:operator_div])
            number2 = int(calc[operator_div + 1:])
            if number2 == 0:
                print("Fehler! Man darf nicht durch null Teilen")
            else:
                result = number1 / number2
                print(result)
    except:
        print("Fehler! Bitte gebe eine gültige Rechnung ein oder 'x' um das programm zu beenden")