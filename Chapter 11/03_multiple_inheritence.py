class Employee:
    company = "VISA"
    eCode = 120
class Freelancer:
    company = "FIVERR"
    level = 0
    def upgradeLevel(self):
        self.level = self.level+1

class Programmer(Employee, Freelancer):     #the class is written first is employee so p.company will print visa first
    name = "Roy"

p = Programmer()
print(p.level)
print(p.company)
p.upgradeLevel()
print(p.level)
