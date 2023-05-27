class Employee:
    company = "Gooogle"
    def __init__(self, name ,salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f'The name of the employee is {self.name}')
        print(f'The salary of the employee is {self.salary}')
        print(f'The subunit of the employee is {self.subunit}')
    
    def getSalary (self, signature):
        print(f'Salary for this employee working in {self.company} is {self.salary}\n{signature}')
    @staticmethod         #if we don't use self
    def greet():
        print("Good Morning, Sir")
roy =Employee("Protoy", 100, "Youtube")
# roy = Employee()  #-->this throws an error(missing three requirted position arguments)
roy.getDetails()