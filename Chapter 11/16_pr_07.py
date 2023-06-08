# Define a custom exception for vector length error
class VectorLengthError(Exception):
    pass

# Define the Vector class
class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"  # Create a string representation of the vector
            index += 1
        return str1[:-1]  # Remove the extra '+' at the end
    
    def __add__(self, vec2):
        if len(self.vec) != len(vec2.vec):  # Check if vector lengths are not compatible
            raise VectorLengthError("Vector lengths are not compatible for addition.")
        
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])  # Add corresponding elements of the vectors
        return Vector(newList)
    
    def __mul__(self, vec2):
        result = 0
        for i in range(len(self.vec)):
            result += self.vec[i] * vec2.vec[i]  # Calculate the dot product of the vectors
        return result

    def __len__(self):
        return len(self.vec)  # Return the length of the vector


# Create vector instances
v1 = Vector([1, 4, 6, 4])
v2 = Vector([1, 6, 9])

try:
    v3 = v1 + v2  # Add v1 and v2
    print(v3)
except VectorLengthError as e:
    print(str(e))  # Print the error message if vector lengths are not compatible

print(len(v1))
print(len(v2))
