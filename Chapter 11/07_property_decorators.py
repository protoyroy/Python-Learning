class Employee:
    company = "Bharat Gas"
    salary = 30000
    salarybonus = 3500
    # totalSalary = 33500

    @property    #to sum total salary (instead of change tottal salary every time we can do that) 
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    @totalSalary.setter    #to change salary bonus according to total salary
    def totalSalary(self, val):
        self.salarybonus = val -self.salary
e = Employee()
print(e.totalSalary)
e.totalSalary = 55000 #to change salary and salary bonus
print(e.salary)
print(e.salarybonus)