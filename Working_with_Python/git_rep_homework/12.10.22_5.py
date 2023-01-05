import math
x = int(input("Input x coordinate of the first point"))
y= int(input("Input y coordinate of the first point"))
x2= int(input("Input x2 coordinate of the second point"))
y2= int(input("Input y2 coordinate of the second point"))
result = math.sqrt(pow(x2-x,2)+pow(y2-y,2))
print(round(result,3))