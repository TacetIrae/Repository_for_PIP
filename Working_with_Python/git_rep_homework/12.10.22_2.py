length = 3
x_y_z = ["X", "Y", "Z"]
my_list = []
for i in range(length):
    my_list.append(input(f"Enter values of {x_y_z[i]}: "))

left = not (my_list[0] or my_list[1] or my_list[2])
right = not my_list[0] and not my_list[1] and not my_list[2]
result = left == right

if (result == True):
    print("Statement is true")
else:
    print("Statement is false")