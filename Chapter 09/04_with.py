with open ('Chapter 09/another.txt', 'r') as f:
    a = f.read()
print(a) 
##we don't need to write f.close (if we use with statement)