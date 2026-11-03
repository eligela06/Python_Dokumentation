numbers = []
for i in range(1,6):
    num = int(input("Enter a number: "))
    numbers.append(num)

print(numbers)
biggest = int(numbers[0])

for i in numbers:

    if i > biggest:
        biggest = i

print(biggest)