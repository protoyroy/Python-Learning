mark1 = float(input("Enter your marks\n"))
mark2 = float(input("Enter your marks\n"))
mark3 = float(input("Enter your marks\n"))
mark4 = float(input("Enter your marks\n"))
mark5 = float(input("Enter your marks\n"))
total = mark1 + mark2 + mark3 + mark4 + mark5
avg =total/5
if avg>=80 and avg<=100:
    print("A+")
elif avg>=70 and avg<=79:
    print("A")
elif avg>=60 and avg<=69:
    print("A-")
elif avg>=50 and avg <=59:
    print("B")
elif avg>=40 and avg<=49:
    print("C")
elif avg>=33 and avg<=39:
    print("D")
else:
 print("Fail")