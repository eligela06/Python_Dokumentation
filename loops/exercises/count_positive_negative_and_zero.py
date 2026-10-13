numbers = []
for i in range(1,6):
    num = int(input("Enter a number: "))
    numbers.append(num)
    
positive = 0
negative = 0
zero = 0


for i in numbers:
    if i == 0:
        zero+= 1
    elif i < 0:
        negative += 1
    elif i>0:
        positive += 1

print(positive,negative,zero)
    