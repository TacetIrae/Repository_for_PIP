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

def MultiResult(list):
    firstPos = 0
    lastPos = 0
    resultList = []
    index = len(list) // 2
    result = 0
    count = 0
    while (index > count):
        firstPos = list[count]
        lastPos = list[len(list)-1-count]
        result = firstPos * lastPos
        resultList.append(result)
        count += 1
    print(resultList)


my_list = ListCreation()
MultiResult(my_list)



