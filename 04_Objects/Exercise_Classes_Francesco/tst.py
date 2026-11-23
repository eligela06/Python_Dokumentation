class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"


person = Person("Elia")
print(person)