def splitting (n):
    ans = []
    d = 2
    while d*d<=n:
        if n%d==0:
            ans.append(d)
            n //=d
        else:
            d +=1
    if n>1:
        ans.append(n)
    return ans


try:
    n = int(input("Enter a number you want to split into multiplies"))
except (TypeError):
    print ("Wrong input")
else:
    print ("Something went wrong")
my_list = []
my_list = list(set(splitting(n)))
print(my_list)