day = int(input("Please enter the number of the day, where 1 is monday and 7 is sunday."))

if (day>5 and day<8):
    print("It is a holiday")
elif (day>0 and day<6):
    print("It is a working day")
else:
    print("Invalid input")