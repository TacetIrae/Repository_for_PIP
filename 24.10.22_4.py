from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios

def polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    poly = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in poly:
        x.append(' + ')
    poly = list(itertools.chain(*poly))
    poly[-1] = ' = 0'
    return "".join(map(str, poly)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = polynomial(k, ratios)
print(polynom1)

with open('33_Polynomial.txt', 'w') as data:
    data.write(polynom1)
