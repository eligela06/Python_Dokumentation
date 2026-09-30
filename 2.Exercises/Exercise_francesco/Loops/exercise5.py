secret_number = 7

while True:
    number = int(input("Input a Number: "))
    if secret_number == number:
        print("You found the secret Number!")
        break
    elif secret_number < number:
        print("too high")
    elif secret_number > number:
        print("too low")