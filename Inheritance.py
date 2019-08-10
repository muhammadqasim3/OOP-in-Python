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


class Programmer(Employee):
    def __init__(self, fname, lname, salary, prog_language, experience):
        super().__init__(fname, lname, salary)
        self.prog_language = prog_language
        self.experience = experience

    def increase(self):
        self.salary = int(self.salary + (Employee.increment + 0.2))


class Trainee(Programmer):
    def __init__(self, fname, lname, stipend, prog_language, duration):
        super().__init__(fname, lname, stipend, prog_language, duration)
        self.duration = duration
        self.stipend = stipend

# print(Employee.is_open("Sunday"))
# obj1 = Employee("Ali", "Ahmed", 40000)


trainee1 = Trainee("Ali", "Hassan",  8000, "Python",  "3 Months")
print(trainee1.salary)
print(trainee1.duration)
print(trainee1.stipend)
print(trainee1.salary)