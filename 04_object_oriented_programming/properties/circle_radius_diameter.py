from math import pi


class Circle:
    def __init__(self, *, radius=None, diameter=None, circumference=None):
        given_values = [radius, diameter, circumference]
        if sum(value is not None for value in given_values) != 1:
            raise ValueError("Gib genau einen Wert an: radius, diameter oder circumference.")

        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = circumference / (2 * pi)

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def circumference(self):
        return 2 * pi * self.radius


c = Circle(diameter=5)
print(c.radius)
print(c.diameter)
print(c.circumference)

