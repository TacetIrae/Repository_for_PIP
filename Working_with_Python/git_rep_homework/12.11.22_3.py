import random

def list_creating(length,min, max):
    my_list = []
    for i in range(length):
        number = random.randint(min,max)
        my_list.append(number)
    return  my_list
def final_list(my_list,length):
    final_list = []
    for i in range(length-1):
        if my_list[i]>my_list[i+1]:
            final_list.append(my_list[i])
    return final_list



len = int(input("Enter length of list you want to generate"))
min_val_list = int(input("Enter min range you want your list to generate"))
max_val_list = int(input("Enter max range you want your ist to generate"))
list = list_creating(len,min_val_list,max_val_list)
print(list)
print(final_list(list,len))
