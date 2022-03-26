"""
When you create derived classes, theses new classes have all the properties of the parent classes plus anything
additional that you write
"""


class Employee:
    def __init__(self, frname, lname, salary):
        self.idnum: int
        self.frname = frname
        self.lname = lname
        self._salary = salary
        self.benefits = 1000

    def get_salary(self):
        return self._salary

    def get_frname(self):  # There is no reason to get a not 'private' variable using get
        return self.frname


class TempEmployee(Employee):
    def __init__(self, frname, lname, salary, idnum):
        super().__init__(frname, lname, salary)
        self.test = 567
        print('ok')



employee1 = TempEmployee('Bruno', 'Silva', 1000.0, 1)
#print(employee1.frname)
print(employee1.benefits)
# print(employee1.get_salary())
print(employee1.lname)
#print(employee1.idnum)
print(employee1.get_salary())
print(employee1.get_frname())
