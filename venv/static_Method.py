# Static method tab use karty hyn jb instance or class dono variables sy kaam nahi hota.
# Static method by default koi argument nahi leta.
# Static method indepent hota hy or apni marzi sy use kar sakty hyn.

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


    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


    # Static method use karyn gy to check whether office is open or closed.
    @staticmethod
    def is_open(day):
        if day.lower() == "sunday":
            return "OFF"
        else:
            return "OPEN"

print(Employee.is_open("Sunday"))

#obj1 = Employee("Ali", "Ahmed", 40000)
#obj2 = Employee("Qasim", "Aslam", 50000)
#print("Before Increment")
#print(obj1.salary)
#print(obj2.salary)
#Employee.change_increment(2)
#obj1.increase()
#obj2.increase()
# obj2.change_increment()
#print("After Increment")
#print(obj1.salary)
#print(obj2.salary)

