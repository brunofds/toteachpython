"""
Applying the factory pattern explained on ArjanCodes channel
https://www.youtube.com/watch?v=s_4ZrtQs8Do
THe factory pattern separate creation from use
"""

class Employee():
    def __init__(self, frname, lname, salary):
        self.idnum: int
        self.frname = frname
        self.lname = lname
        self._salary = salary
        self.benefits = 1000

    def getSalary(self):        # method of Employee class
        return self._salary


# There can be many instances of a class, each holding different values

person1 = Employee("Bruno", "Silva", 1300)  # person1 is an instance of Employee class and also called an object
print(person1.getSalary())

person2 = Employee("Larissa", "Guti", 8000)
print(person2.getSalary())

'''
Instead use 'getSalary', it's possible to use the class variables directly.
'''
print(person1._salary)

'''
If you have this directly option to access values, why bother with accessor functions?
It is partly to emphasize that the variables inside the class are private and the implementation might change
There is a Python convention that you name these private variables with a leading underscore, to emphasize that you 
aren't meant to access them directly. This makes them harder to type accidentally. 
'''


