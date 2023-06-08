class Vector:
    def __init__(self,vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index +=1
        return str1[ :-1]   #we do it otherwise it will come extra + in tthe end
    
    def __add__(self, vec2):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self,vec2):
        result = 0
        for i in range (len(self.vec)):
            result += self.vec[i] *vec2.vec[i] 
        return result

    
v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1+v2)
print(v1*v2)
