

def list_generation (length):
    my_list_odd = []
    for i in range(0,length+1):
        if i%2==1:
            my_list_odd.append(i)
    return my_list_odd

len_list = int(input("Enter a maximum number you want your list to be created until"))
sqrt_max_value = int(input("Enter a number that will determine the maximum value of the square root of the numbers thst are generated within the sequence that you set up"))
my_list = list_generation(len_list)
print(my_list)

final_list = [var for var in my_list if var ** 2 <= sqrt_max_value]

print(f"Final list is: {final_list}")


