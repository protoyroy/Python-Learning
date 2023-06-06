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

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1

n = Number(24)
print(n)
print(len(n))

#str method & length mthodto understand fully
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        Custom string representation of the Person object.
        """
        return f"Person(name={self.name}, age={self.age})"

    def __len__(self):
        """
        Define the length as a tuple with the lengths of the name and age attributes.
        """
        name_length = len(self.name)
        age_length = len(str(self.age))
        return name_length + age_length

# Create a Person object
person = Person("John Doe", 25)

# Get the lengths of the name and age attributes in the Person object
total_length = len(person)

# Print the lengths
print(total_length)




