class Employee:
    company = "Gooogle"
    def getSalary (self, signature):
        print(f'Salary for this employee working in {self.company} is {self.salary}\n{signature}')
    @staticmethod         #if we don't use self
    def greet():
        print("Good Morning, Sir")

protoy = Employee()
protoy.salary = 100000
protoy.getSalary("Thanks!")    #Employee.getSalary(protoy)
protoy.greet()