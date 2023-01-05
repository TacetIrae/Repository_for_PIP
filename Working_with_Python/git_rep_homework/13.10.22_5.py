#Реализуйте алгоритм перемешивания элементов списка.
# Без функции shuffle из модуля random, другие методы использовать можно.
import random
from random import randint
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

def list_shuffle (list):
    j = len(list)
    for i in range(j):
        random = randint(i, j-1)
        list[i],list[random] = list[random], list[i]
    return list

my_list = ListCreation()
print(f"Shuffled list is the following:{list_shuffle(my_list)} ")

