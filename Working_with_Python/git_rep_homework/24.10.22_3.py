def list_creation (list_length):
    my_list = []
    for i in range(list_length):
        number = int(input(f"Enter {i} number of the sequence"))
        my_list.append(number)
    return my_list
count = int(input("Enter a number of numbers that will be included in the sequence"))
my_list = list_creation(count)
my_list = list(set(my_list))
print(my_list)