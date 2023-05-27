
class Employee:
    company = "Google"
    salary = 800000

protoy = Employee()
rahul = Employee()
binod = Employee()   #it will automatically take the class salary
protoy.salary = 30000  #instance attributes
rahul.salary = 50000
print(protoy.company)
print(rahul.company)
print(binod.company)
Employee.company = "Youtube"    #to change company name
print(protoy.company)
print(rahul.company)
print(protoy.salary)
print(rahul.salary)
print(binod.salary)
