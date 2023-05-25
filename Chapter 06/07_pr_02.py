sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% percentage in one of the subjects\nBetter luck next time")

elif(sub1+sub2+sub3/3 <40):
    print("You are fail due to total percentage is less than 40")

else:
    print("Congratulatiopns!\nYou are passed")
