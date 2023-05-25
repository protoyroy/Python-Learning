number = int(input("Enter the number: "))

print("Multiplication Table of", number)
for i in range(1, 11):
    product = number * i
    print(number, "x", i, "=", product)
