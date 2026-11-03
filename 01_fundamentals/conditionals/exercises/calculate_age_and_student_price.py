age = int(input("How old are you?"))
student = input("Are you a student?(y/n)").strip().lower()

price = 12

if age < 12:
    price = 7

elif age < 17:
    price = 9

if student == "y":
    price -= 2 

print(f"Price: {price}")

