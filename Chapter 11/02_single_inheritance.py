class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")


class Programmer(Employee):
    language = "Python"
    company = "Youtube"
    def getLanguage(self):
        print(f"The language is{self.language}")
    def showDetails(self):
        print("This is a programmer")


a = Employee()
a.showDetails()

p= Programmer()
p.showDetails()
print(p.company)
print(p.language)