class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
protoyApplication = RailwayForm()
protoyApplication.name = "Protoy"
protoyApplication.train = "Nilsagor"
protoyApplication.printData()