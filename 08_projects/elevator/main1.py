import time

class Elevator:
    def __init__(self,num):
        self.num = num
        self.floor = 0
        self.distance = 0



    def drive(self, target):
        while self.floor != target:
            print(self.floor)
            if self.floor > target:
                self.floor -= 1
            else:
                self.floor += 1
            time.sleep(2)
        print(self.floor)

    def calculate_distance(self, target):
        if self.floor > target:
            return self.floor - target
        else:
            return target - self.floor


class Person:
    def __init__(self, floor):
        self.floor = floor

def calculate_faster_elev(elev1, elev2):
    if elev1.calculate_distance(person_1.floor) < elev2.calculate_distance(person_1.floor):
        return elev1
    else:
        return elev2


elevator_1 = Elevator(1)
elevator_2 = Elevator(2)

person_1 = Person(4)

elevator_1.floor = 4






while True:
    x = input("Press Enter to call the elevator: ")
    faster_elev = calculate_faster_elev(elevator_1, elevator_2)
    print("Elevator: ", faster_elev.num)
    faster_elev.drive(person_1.floor)
    choice = int(input("On wich floor do you wanna go(0,1,2,3,4): "))
    faster_elev.drive(choice)
    person_1.floor = choice
    print("Bye Bye")
    print(f"Elevator1: {elevator_1.floor}, Elevator2: {elevator_2.floor}, Person: {person_1.floor}")