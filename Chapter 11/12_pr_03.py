#salaryAfterincrement = salary * increment 9this is the formula)
class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary
e= Employee() 
e.salaryAfterIncrement = 2000
print(e.salaryAfterIncrement)
print(e.increment)
