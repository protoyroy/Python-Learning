class Programmer:
    company = "Micrposoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

roy = Programmer("Protoy", "Skype")
rani = Programmer("Rani", "Github")
roy.getInfo()
rani.getInfo()
