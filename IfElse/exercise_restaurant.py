price = 0
age = int(input("Write your age: "))
drink = input("Write wich drink you want: ").strip().upper()

if drink == "W":
    drink = "Water"
    price = 2
elif drink == "J":
    drink = "juice"
    price = 3
elif drink == "C":
    drink = "coffee"
    price = 4
elif drink == "T":
    drink = "tee"
    price = 3
else:
    print("Invalid input")

print(f"Drink: {drink}")

if age < 12 and drink == "coffee":
    print("your not allowed to drink coffe")

elif age < 12:
    price -= 1

print(f"Price: {price}")