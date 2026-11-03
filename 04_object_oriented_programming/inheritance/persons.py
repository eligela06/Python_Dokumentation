class Person():
    def __init__(self, name):
        self._name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

person = Person("Elia")
person1 = EmailPerson("Lenny", "lenny.bischof@icloud.com")

print(person1._name)