x = int(input("Enter x coordinate"))
while (x == 0 ):
    print("X can not be = to 0")
    x = int(input("Enter x coordinate"))
y = int(input("Enter y coordinate"))
while (y==0):
    print("Y can not be = to 0")
    y = int(input("Enter y coordinate"))

if (x>0 and y>0):
    print("First quarter")
elif (x<0 and y>0):
    print("Second quarter")
elif (x<0 and y <0):
    print ("Third quarter")
elif (x>0 and y<0):
    print("Fourth quarter")
else:
    print("Invalid input")