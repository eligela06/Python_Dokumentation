def make_counter():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

c = make_counter()
print(c())
print(c())
print(c())