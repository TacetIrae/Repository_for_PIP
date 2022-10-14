#Задайте список из элементов, заполненных числами из промежутка [-N, N].
# Задайте два числа - позиции(индексы) в исходном списке это границы диапазона.
# Найдите произведение элементов списка в указанном диапазоне индексов
import random
def ListCreation ():
    while (True):
        try:
            upper = int(input("Enter upper N value"))
        except ValueError:
            print("Incorrect input")
            continue
        else:
            print(f"Your upper limit is {upper}")
            break
    while (True):
        try:
            lower = int(input("Enter lower N value"))
        except ValueError:
            print("Incorrect input")
            continue
        else:
            print(f"Your lower limit is {lower}")
            break
    while (True):
        try:
            list_size = int(input("Enter the size of the list"))
        except ValueError:
            print("Incorrect input")
            continue
        else:
            break
    count = 0
    my_list = []
    while (list_size>count):
        my_list.append(random.randint(lower,upper))
        count += 1
    print (f"List is following: {my_list}")
    return my_list



def SortingList (list):
    while (True):
        try:
            upper = int(input("Enter upper N value"))
        except ValueError:
            print("Incorrect input")
            continue
        else:
            print(f"Your upper limit is {upper}")
            break
    while (True):
        try:
            lower = int(input("Enter lower limit N value of sorted list"))
        except ValueError:
            print("Incorrect input")
            continue
        else:
            print(f"Your lower limit is {lower}")
            break
    sorted_list = []
    count = 0
    while (len(list)>count):
        if (list[count] < upper and list[count] > lower):
            sorted_list.append(list[count])
        count += 1
    sorted(sorted_list)
    print(f"Sorted list is: {sorted_list}")
    return sorted_list

def SumOfTheList (list):
    sum = 0
    count = 0
    while (len(list)>count):
        sum = sum +list[count]
        count += 1
    return sum

my_list = ListCreation()
print("Now that the list is a created, we will proceed with cutting it down with user settings")
sorted_list = SortingList(my_list)
print(f"Here is the sum of the numbers within the list: {SumOfTheList(sorted_list)}")

