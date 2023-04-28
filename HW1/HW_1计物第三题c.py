import numpy
def term(n):
    sum = 0
    for i in range(2, n):
        for r in range(2, i+1):
            sum = sum+numpy.math.log(r)
    return sum


print('n ln(det) det')
for n in range(1, 11):
    lndet = 4*term(n)-term(2*n)
    print(f'{n} {lndet:.3e} {numpy.math.e**lndet:.3e}')