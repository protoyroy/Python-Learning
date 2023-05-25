myDict = {
   "fast":"In a quick manner",
   "protoy": "A Coder",
   "marks":[1,2,3,4],
   "anotherdict":{"Protoy":"player"},
    1:2
}
print(myDict.keys())        #whats inside in the mydict
print(type(myDict.keys()))     #to find dictonary type
print(list(myDict.keys()))      #to make it list
print(myDict)
updateDict ={
    "Love" : "Friends",
    "X":"y",
    "protoy": "A Dancer",
    
}
myDict.update(updateDict)     #update the dictonary by adding key-value paris from updateDict
print(myDict.values())
print(myDict.get("Protoy"))      #Print value associated with Protoy
print(myDict["protoy"])        #Print value associated with Protoy
##The difference between .get and [] syntax in dictonaries
print(myDict.get("Protoy2"))         #return none as protoy2 is not present in the dictonary
print(myDict["protoy2"])       #throws an error as protoy2 is not present in the dictonary