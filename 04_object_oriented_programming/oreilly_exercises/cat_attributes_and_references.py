class Cat():
    def __init__(self, name):
        self.name = name
    

a_cat = Cat('')
another_cat = Cat('')

a_cat.age = 3
a_cat.name = "Caty"
a_cat.nemesis = another_cat
a_cat.nemesis.name = "Robert"
print(a_cat.name, a_cat.age, a_cat.nemesis.name)

new_cat = Cat(name='Mina')
print(new_cat.name)