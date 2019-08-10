class Employee:
    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 2.0

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        return 'Employee name is {}'.format(self.fname)


obj1 = Employee("Ali", "Ahmed", 40000)
obj2 = Employee("Qasim", "Aslam", 50000)

print(obj1.salary)
print(obj2.salary)
print(obj1.salary + obj2.salary)
print(repr(obj1))
print(str(obj1))

