class Employee:
    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 2.0

    def increase(self):
        # self.salary = self.salary * self.increment
        self.salary = int(self.salary * Employee.increment)


obj1 = Employee("Ali", "Ahmed", 40000)
obj2 = Employee("Qasim", "Aslam", 50000)
print("Before Increment")
print(obj1.salary)
print(obj2.salary)
obj1.increase()
obj2.increase()
print("After Increment")
print(obj1.salary)
print(obj2.salary)

