myDict ={
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("options are",myDict.keys())
a = input(" Enter the hindi words\n")

#Below line will not throw an error if its not available in dictonary
print(" The meaning of your word is",myDict.get(a))