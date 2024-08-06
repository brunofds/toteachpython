

class Temperature:
    def __init__(self, temp):
        self.celsius = temp
        self.test = None

    def to_farenheit(self):
        return self.celsius * 1.8 + 32


human = Temperature(37)
print(human.to_farenheit())

print(human.__dict__['celsius'])
