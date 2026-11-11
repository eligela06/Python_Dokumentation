from pathlib import Path

datei_pfad = Path(__file__).with_name("first_generator.py")

with datei_pfad.open("r", encoding="utf-8") as datei:
    print(datei.read())


# def foo():
#     yield 1

# lst = [1]

# x = foo()
# print(next(x))

# print(next(lst))

# def fib():
#     a, b = 1,1
#     yield 1
#     yield 1
#     while True:
#         a, b = b, a+b
#         yield b


# for n in fib():
#     print(n)

# def one():
#     raise ValueError("Value error")

# try:
#     one()
# except ValueError as i:
#     print("boom")
#     print(i)
# except TypeError:
#     print("kaboom")
# finally:
#     print("YES")