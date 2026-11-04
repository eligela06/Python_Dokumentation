def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
ranger = my_range(0,120)

for x in ranger:
    print(x)

abc = ['']
for code in range(ord('A'), ord('z') + 1):
    abc.append(chr(code))
print(abc)
print(abc.index('A'))