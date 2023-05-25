n = int(input("Enter the number\n"))
sum = 0
if n < 0:
   print("Enter a positive number")
while(n>0):
    sum = sum+n
    n= n-1
    print(" The sum of first n natural number is", sum)