import random 

def generat_random(a=0,b=1):
    return random.randint(a,b)

def add(a,b):
    return a+b

def mult(a,b):
    return a*b

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.name = lastname
        self.fullname = name + ", " + lastname

    def __str__(self):
        return self.fullname

class Employe(Person):
    def __init__(self, name, lastname, salary):
        super().__init__(name, lastname)
        self.salary = salary