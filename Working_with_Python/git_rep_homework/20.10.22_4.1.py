number = int(input("Enter a number"))

def DecimalBinary (num):
    if num >= 1:
        DecimalBinary(num//2)
    print(num%2,end ='')

DecimalBinary(number)