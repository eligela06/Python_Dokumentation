# class Person:
#     pass

# new_person = Person()
# new_person.name = "Elia"
# new_person.age = 15

# print(f"{new_person.name}, {new_person.age}")
class AgeException(Exception):
    pass

class Person:
    def __init__(self, first_name=None, last_name=None, age=None):
        if age==None or first_name==None or last_name==None:
            raise ValueError("Values can't be Empty")
        
        if type(age) != int or type(last_name) != str or type(first_name) != str:
            raise ValueError("Type first your name(string) and then your age(integer)")
        
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.age = age


    def print_values(self):
        print(f"Name: {self.last_name}, {self.first_name}")
        print(f"Age: {self.age}")
        print(f"You can drive: {self.can_drive()}")

    def can_drive(self):
        return (self.age >= 18)

class Child(Person):
    def __init__(self, first_name=None, last_name=None, age=None):
        super().__init__(first_name, last_name, age)
        if self.age >= 16:
            raise AgeException("Your not a Child anymore")

new_person = Person("ELia", "bIschof", 18)
new_person.print_values()

new_child = Child("Lenny", "biSChoF", 14)
new_child.print_values()