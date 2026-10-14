class Car():
    def __init__(self, sound):
        self.sound = sound
    def make_sound(self):
        print(self.sound)

class Toyota(Car):
    pass

new_car = Toyota("Wrumm")


new_car1 = Car("Nium")

cars = []
cars.append(new_car)
cars.append(new_car1)

for car in cars:
    car.make_sound()