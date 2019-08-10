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

    # class variable ko direct change karny k bajaye uska ek method bana kar dynamic kar dyn
    # class method tab use karty hyn jab instance ka koi kaam nahi hota yani instance k attributes ko change nahi karna hota sirf class k variables ko change karna hota hy.

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


obj1 = Employee("Ali", "Ahmed", 40000)
obj2 = Employee("Qasim", "Aslam", 50000)
print("Before Increment")
print(obj1.salary)
print(obj2.salary)
Employee.change_increment(2)
obj1.increase()
obj2.increase()
#obj2.change_increment()
print("After Increment")
print(obj1.salary)
print(obj2.salary)

