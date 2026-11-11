temps_c = [-5, 0, 18, 25, 37]

def to_fahrenheit(c):
    return c * 9 / 5 + 32.


def describe(c):
    fahrenheit = to_fahrenheit(c)
    return f"{c}°C = {fahrenheit}°F"

for temp in temps_c:
    print(describe(temp))
