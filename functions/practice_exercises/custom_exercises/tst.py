def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)




def fib1(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(n-2):
        t = a+b
        a = b
        b = t
    return b

print(fib1(7))