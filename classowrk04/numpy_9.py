import numpy as np
def prime_number(k=0):
    numb = 0
    count=1
    while numb < k:
        count += 1
        condition = 1
        for i in range(2, count):
            if count%i == 0:
                condition = 0
        if condition == 1:
            numb += 1
            prime = count
    return prime
def fibonacci_number(k=0):
    numbe = [1, 1, 2]
    for i in range(k-1):
        numbe[i%3] = numbe[(i+1)%3] + numbe[(i+2)%3]
    return(numbe[(k-1)%3])
vecprim = np.array([-prime_number(i) for i in range(1, 11)])
vecfib = np.array([fibonacci_number(i) for i in range(1, 11)])
print(np.dot(vecfib, vecprim))
