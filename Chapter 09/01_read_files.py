##use open function to read the content of a file
f= open('Chapter 09/sample.txt', 'r')  # r to read file
# f = open ('Chapter 09/sample.txt') #by default r
# data = f.read()
data = f.read(5) # read first five character from ther file
print(data)
f.close()

##  this is a checking code by me(not correct ig)
# f = open('Chapter 09/sample.txt', 'w')
# writen = "This is a good text"
# data = f.write(writen)
# print(data)
# f.close()
