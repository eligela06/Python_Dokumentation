Numbers = []

def input_number():
    value = input("Enter a Number (or q to quit): ")
    if value.lower() == "q":
        return False
    try:
        Numbers.append(int(value))
    except:
        return False
    return True

while True:
    if not input_number():
        break

Numbers.sort()
print(Numbers)