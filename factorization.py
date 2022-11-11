import math
import sys

sqrt_int = lambda x: int(math.sqrt(x))

# Fatoração do luizil
def fatores_primos(n):
    fatores = []
    c = n
    while ((c % 2 == 0)):
    
        fatores.append(2)
        c = c / 2
    
    i = 3
    while (i <= math.sqrt(c) + 1):
    
        if (c % i == 0):
        
            fatores.append(i)
            c = c / i
        
        else:
            i = i + 2
    
    if (c > 1):
        fatores.append(c)
    
    return fatores
   
# Fatoração utilizando fermat
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
