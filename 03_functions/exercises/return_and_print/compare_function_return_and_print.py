def square(n):
    return n**2

a = square(3)
b = square(4)

print(a+b)

def bad_square(n):
    print(n**2)

result = bad_square(3)
print(result)