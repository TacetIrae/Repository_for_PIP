# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
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

def SortList (list):
    sortedOddList = []
    sortedEvenList = []
    for i in range(len(list)):
        if (list[i] % 2 == 1):
            sortedOddList.append(list[i])
        elif (list[i] % 2 == 0):
            sortedEvenList.append(list[i])
        else:
            print("Something went wrong")

    print(f"Odd list{sortedOddList} and Even list{sortedEvenList}")
    return sortedOddList,sortedEvenList


def SumOfLists(listOdd,listEven):
    OddSum = 0
    EvenSum = 0
    for i in range (len(listOdd)):
        OddSum = OddSum + listOdd[i]
    for j in range (len(listEven)):
        EvenSum = EvenSum + listEven[i]
    print(f"Sum of the odd numbers = {OddSum} and Sum of the even: {EvenSum}")

my_list = ListCreation()
OddList, EvenList = SortList(my_list)
SumOfLists(OddList,EvenList)