class Person:
    def __init__(self,name, age, salary=None):
        self.name = name
        self.age = age
        self.salary_per_hour = salary

    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age} \nSalary: {self.salary_per_hour}.CHF "
    
    def work(self, hours):
        return hours * self.salary_per_hour

class Bankaccount(Person):
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def __str__(self):
        return f"Owner: {self.owner.name} \nAccount balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
    
    def take_off(self, amount):
        if amount > self.balance:
            print("Your balance is to low!")
        else:
            self.balance -= amount
            print(f"Balance: {self.balance}")
        

person = Person("Elia", 15, 5)


person_bank_account = Bankaccount(person)


person_bank_account.deposit(person.work(5))

print(person_bank_account)

person_bank_account.take_off(2)