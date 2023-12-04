"""
Class 32 - Multiple Inheritance
https://www.programiz.com/python-programming/multiple-inheritance
Python does allow Multiple Inheritance
Be careful with tha name collisions
"""


class Vehicle:

    def __init__(self):
        self.speed = 0

    def drive(self, speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed = 0
        print('Stopped')

    def display(self):
        print(f'Driving at {self.speed} speed')


class Freezer:

    def __init__(self):
        self.temp = 0

    def freeze(self, temp):
        self.temp = temp
        print('Freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')


# Using Multiple Inheritance
class TruckFreezer(Vehicle, Freezer):
    # It uses the Method Resolution Order (MRO). First comes first (Vehicle comes first)

    def display(self):
        print(f'Is a freezer: {issubclass(TruckFreezer, Freezer)}')
        print(f'Is a vehicle: {issubclass(TruckFreezer, Vehicle)}')

        # super(Vehicle, self).display()  # Works because of MRO
        # super(Freezer, self).display()  # Fails because of MRO

        # If we want to use both of methods with the same name, we have to independently call them
        Freezer.display(self)
        Vehicle.display(self)


test = TruckFreezer()
test.freeze(-30)
test.drive(50)
# test.stop()
test.display()
