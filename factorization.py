import math
import sys

sqrt_int = lambda x: int(math.sqrt(x))
 
def fermat(number):
    factors = []
    while number % 2 == 0:
        number = number/2
        factors.append(2)
 
    if number == 1:
        return factors
 
    r = sqrt_int(number)
    for r in range(sqrt_int(number), int((number+1)/2)):
        m = (r ** 2) - number
 
        if m >= 0 and math.sqrt(m) == math.floor( math.sqrt(m) ):
            s = sqrt_int(m)
            factors = factors + fermat(r - s)
            factors = factors + fermat(r + s)
            break
    else:
        factors.append(number)

    return factors
 
 
number = int(sys.argv[1])
 
print(fermat(number))
