class Employee:
    company = "Gooogle"
    def getSalary (self):
        print(f'Salary for this employee working in {self.company}  is {self.salary}')

protoy = Employee()
protoy.salary = 100000
protoy.getSalary()
# Employee.getSalary(protoy)