class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __mul__(self, timesheet):
        print("worked for", timesheet.days,"days")
        #calculate salary
        return self.salary * timesheet.days
class Timesheet:
    def __init__(self, name , days):
        self.name = name
        self.days = days
emp = Employee("Ahmed", 800)
timesheet = Timesheet("ahmed",50)
print("salary is: ", emp * timesheet)
    