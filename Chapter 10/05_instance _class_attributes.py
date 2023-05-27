class Employee:
    company = "Google"
    salary = 800000

protoy = Employee()
rahul = Employee()
binod = Employee()   #it will automatically take the class salary because binod's salary is not mentioned
#Creating instance salary(first it checks instance value )
protoy.salary = 30000  
rahul.salary = 50000
print(protoy.salary)
print(rahul.salary)
print(binod.salary)        