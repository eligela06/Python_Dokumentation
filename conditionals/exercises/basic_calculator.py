operaters = ["+","-","/","*"]
number = int(input("Write a number: "))
operation = (input(f"Write a operation{operaters}: ")).strip()
number1 = int(input("Write a number: "))

if operation in operaters:
    if operation == "+":
        result = number + number1
    elif operation == "-":
        result = number - number1
    elif operation == "*":
        result = number * number1
    elif operation == "/":
        result = number / number1
    print(number, operation, number1, "=", result)
else:
    print("not a valid operator")