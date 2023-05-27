class Sample:
    a = "Protoy"

obj = Sample()
obj.a = "Roy"
Sample.a = 'Roy' #If I want to change class attributes (means if want to change  protoy to Roy)

print(Sample.a)
print(obj.a)