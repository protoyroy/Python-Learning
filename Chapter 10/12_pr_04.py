class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        print(f'The value of {self.number} is {self.number **2}')

    def squareRoot(self):
       print(f'The value of {self.number} is {self.number **0.5}' )
    def cube(self):
        print(f'The value of {self.number} is {self.number **3}' )
    
    @staticmethod
    def Greet():
        print('*******Hello there welcome to the best calculator in the world!******')

a = Calculator(9)
a.Greet()
a.square()
a.squareRoot()
a.cube()
