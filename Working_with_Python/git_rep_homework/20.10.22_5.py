def fibonacchi (num):
    if num <= 1:
        return num
    return fibonacchi(num-1)+fibonacchi(num-2)


number = int(input("Enter N value"))
my_list_pos = []
my_list_neg = []
for i in range(number):
    my_list_pos.append(fibonacchi(i))
for j in range(len(my_list_pos)):
    my_list_neg.append(my_list_pos[j])
    my_list_neg[j] = my_list_neg[j] * -1
my_list_neg.reverse()
final_list = [*my_list_neg,*my_list_pos]
final_list.remove(0)
print(final_list)



