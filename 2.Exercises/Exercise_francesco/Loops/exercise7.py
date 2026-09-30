number1 = 1
number2 = 1
for number2 in range(1, 6):
    number1 = 1
    for number1 in range(1, 6):
        print(f"{number2} x {number1} = {number1 * number2:2}", end="    ")
    print()