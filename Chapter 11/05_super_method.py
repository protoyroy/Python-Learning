class Person:
    country = "Canada"
    def __init__(self):
        print("Initializing person..\n")
    def takeBreath(self):
        # super().takeBreath()    # here this lines throws an error because nothing is in up of this
        print("I am breathing....")

class Employee(Person):
    company = "BMW"

    def __init__(self):
        super().__init__()
        print("Initializing employee..\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()        #it will first send to first take breath to run
        print("I am breathing luckily")

class Programmer(Employee):
    company = "Google"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer..\n")

    def getSalary(self):
        print(f"No salary to programmer")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer so I am breathing py.")
# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()
