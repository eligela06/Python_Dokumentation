class Car():
    def __init__(self, sound):
        self.sound = sound
    def make_sound(self):
        print(self.sound)

class Toyota(Car):
    pass

new_car = Toyota("Wrum")
new_car.make_sound()