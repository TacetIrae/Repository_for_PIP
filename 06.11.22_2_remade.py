from random import randint

def input_dat(name):
    x = int(input(f"{name}, enter a number of candies that you will pick from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, enter a correct number of candies: "))
    return x

def info(name, k, counter, value):
    print(f"Step made by {name}, took {k}, now he has {counter}. The remaining quantity is {value}.")

def bot_input_data(name):
    x = randint(1,29)
    return x


total_candy = 220
player1 = input("Enter a nickname for first player")
player2= input("Enter a nickname for second player, if you wish to play against bot, please enter 'bot'").lower()

if player2 == 'bot':
    step = randint(0, 2)
    if step == 0:
        print(f"First to take a step is {player1}")
    else:
        print(f"First to take a step is {player2}")
    count_pl_1 = 0
    count_pl_2 = 0

    while total_candy > 28:
        if step:
            k = input_dat(player1)
            count_pl_1 += k
            total_candy -= k
            step = False
            info(player1, k, count_pl_1, total_candy)
        else:
            k = bot_input_data(player2)
            count_pl_2 += k
            total_candy -= k
            step = True
            info(player2, k, count_pl_2, total_candy)
    if step:
         print(f"Plaer {player1} won")
    else:
        print(f"PLayer {player2} won")
    exit()



step = randint(0,2)
if step == 0:
    print(f"First to take a step is {player1}")
else:
    print (f"First to take a step is {player2}")

count_pl_1=0
count_pl_2=0

while total_candy > 28:
    if step:
        k = input_dat(player1)
        count_pl_1 += k
        total_candy -= k
        step = False
        info(player1, k, count_pl_1, total_candy)
    else:
        k = input_dat(player2)
        count_pl_2 += k
        total_candy -= k
        step = True
        info(player2, k, count_pl_2, total_candy)

if step:
    print(f"Plaer {player1} won")
else:
    print(f"PLayer {player2} won")
