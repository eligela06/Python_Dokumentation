numbers = [1,4,6,2,]


largest = numbers[0]

for number in numbers:
    
    if number > largest:
        largest = number

print(largest)

numbers.sort(reverse=True)
print(numbers[0])