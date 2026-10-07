numbers = []
while True:

    x = int(input("Input a Number: "))
    if x == 0:
        print(sum(numbers))
        break
    numbers.append(x)