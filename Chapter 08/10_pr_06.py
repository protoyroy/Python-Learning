def inches_to_cm(inches):
    return inches * 2.54
inches = int(input("Enter incehs:\n"))
cm = inches_to_cm(inches)
print(inches, "inces is equal to", cm, "centimeters")