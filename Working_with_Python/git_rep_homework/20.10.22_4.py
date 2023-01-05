#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
while True:
    try:
        user_input = int(input("Enter a whole number you want to transfer to binary"))
    except ValueError:
        print("Incorrect input")
        continue
    else:
        break
result = format(user_input,"b")
print(result)