class Sample:
    def __init__(protoy,name):    #if i want to change self it will work instead of self i used (protoy,name)
        protoy.name = name
obj = Sample("Protoy")
obj.a = "Roy"
print(obj.name)