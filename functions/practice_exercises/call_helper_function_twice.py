def double(x):
    return (x * 2)

def quadruple(x):
    double(x)
    double(x)
    return x

print(quadruple(3))