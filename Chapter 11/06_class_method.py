class Employee:
    company = "Zara"
    salary = 1000000
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal #to change class salary
    

  #you can also do that instead of the top line  
    @classmethod
    def changeSalary(x, sal):
        x.salary = sal
e = Employee()
print(e.salary)
e.changeSalary(500000)
print(e.salary)
print(Employee.salary)