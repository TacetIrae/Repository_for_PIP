#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел
#от 1 до N.

def CumulativSum(n):
    count = 1
    sum = 1
    my_list = []
    if (n == 0):
        print("N value = to 0, the further process is impossible")
    else:
        while (n>count-1):
            sum = sum*count
            my_list.append(sum)
            count +=1
    return my_list

while (True):
    try:
        num = int(input("Enter N value"))
    except ValueError:
        print("Incorrect input")
        continue
    else:
        print(f"Your input is {num}")
        break

print(f"The cumulative sum of the n = {CumulativSum(num)}")


