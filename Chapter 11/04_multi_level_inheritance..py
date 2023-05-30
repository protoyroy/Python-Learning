class Person:
    country = "Canada"
    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company = "BMW"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am breathing luckily")

class Programmer(Employee):
        company = "Google"
        
        def getSalary(self):
            print(f"No salary to programmer")
    
        def takeBreath(self):
             print("I am a programmer so I am breathing py.")
p = Person()
p.takeBreath()
# print(p.company) #throws an error
e = Employee()
e.salary = "40K"
e.getSalary()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
pr.getSalary()
print(pr.company)
print(pr.country)