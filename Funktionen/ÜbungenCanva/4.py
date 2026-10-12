def square(n):
    return n**2
square_of_3 = square(3)
square_of_4 = square(4)

print(square_of_3 + square_of_4)

def bad_square(n):
    print(n**2)

result = bad_square(3)
print(result)