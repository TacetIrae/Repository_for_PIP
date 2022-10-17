#Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import math
import numpy as np
def SortingList(list):
    decimalNumbers = []
    for i in range(len(list)):
        x,y = math.modf(list[i])
        decimalNumbers.append(x)
    return decimalNumbers






my_list = [1.01,2.22,10.00,15.11,99.09]
my_list = SortingList(my_list)
my_list = list(np.around(np.array(my_list),2))
my_list.sort()
my_list = [i for i in my_list if i != 0]
result = my_list[len(my_list)-1] - my_list[0]
print(f'Difference between biggest and smallest decimal is :{result}')

