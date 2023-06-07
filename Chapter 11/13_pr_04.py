class ComplexNumber:
    def __init__(self, r , i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return complex(self.real+ c.real, self.imaginary + c.imaginary)

c1 = ComplexNumber(1, 4) #c1 =complex(1,4) i can also write that as complex is a build in function in python
c2 = ComplexNumber(8, 5) #c2 =complex(8,5)
print(c1+c2)