numbers =[]
double = []
how_many_numbers = int(input("Wie viele zahlen willst du eingeben? "))

def add_number():
    for i in range(1,how_many_numbers + 1):
        number = int(input(f"Gib deine {i} Zahl ein: "))
        if number in numbers:
            double.append(number)
        numbers.append(number)

while True:
    try:
        add_number()
        break
    except:
        print("Bitte gib eine Zahl ein!")

print("\n")
print(numbers)
print("\n")

def biggest_number():
    big_number = max(numbers)
    print(big_number)

print("Grösste Zahl:")
biggest_number()
print("\n")

print("Doppelte oder mehrfache Zahlen:")
for i in double:
    print(i)
print("\n")
