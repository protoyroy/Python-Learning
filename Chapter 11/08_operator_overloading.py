class Number:
    def __init__(self, num):
        self.num = num
    
    #add
    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num
   
    #multiply
    def __mul__(self, num2):
        print("Let's multiply")
        return self.num *  num2.num

    #division
    def __truediv__(self, num2):
        print("Let's division")
        return self.num /  num2.num

    #floor division      [Floor division is useful in situations where you want to divide two numbers and obtain an integer result, without considering the decimal part.]
    def __floordiv__(self, num2):
        print("Let's floor")
        return self.num //  num2.num

n1 = Number(24)
n2 = Number(2)
sum = n1 + n2
mul = n1 * n2
div = n1 / n2
floor = n1 // n2
print(sum)
print(mul)
print (div)
print(floor)