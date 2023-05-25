##Creating an empty set
b = set()
b.add(5)        #to add value
b.add(5)        #set is a not-repititive 
b.add(4)

##Accessing elements from set
b.add((4, 5, 6))       #we can add tuple in the set
# b.add([4, 5, 6])        #we can't add list in the sert
# b.add({4, 5})        #we can't add dictonary in set as it is not hasable


print(b)

##To find the length of a set
print(len(b))     #Prints the length of the set

##To remove object from a set
# b.remove(4)         #remove 4 from set
# b.remove (15)       # will show error as it is not in the set
# print(b)

##To remove random value
print(b.pop())          #pop remove random value from the set
print(b)

##to clear the set
print(b.clear())
print(b)