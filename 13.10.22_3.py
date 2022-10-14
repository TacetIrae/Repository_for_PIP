#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
def InputNumber():
    while (True):
        try:
            num = int(input("Enter N value"))
        except ValueError:
            print("Incorrect input")
            continue
        else:
            print(f"Your input is {num}")
            break
    return num
def FuncCalculation(n):
    my_list = []
    count = 1
    sum = 1
    if (n ==0):
        print ("N is equals to 0, sequence can not be produced")
    else:
        while (n> count-1):
            sum = round((1+1/count)**count,2)
            my_list.append(sum)
            count += 1
    return my_list

number = InputNumber()
print(FuncCalculation(number))