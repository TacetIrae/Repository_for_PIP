number = str(input("Enter a number"))
my_list =[]
sum = 0
for i in range(len(number)):
    my_list.append(number[i])
if '.' in my_list:
    my_list.remove(".")
for i in range(len(my_list)):
    num = int(my_list[i])
    sum += num
print(sum)