import numpy as np
def factorial(k):
    s = 1
    if k == 0:
        return 1
    else:
        for i in range(1, k+1):
            s *= i
        return s
def expon(a, b):
    a = np.array(a)
    leng = np.size(a)**0.5
    matr = np.reshape(a, (leng, leng))
    matfin = np.eye(leng)
    mat1 = np.reshape(a, (leng, leng))
    for i in range(1, b+1):
        matfin = matfin + mat1/factorial(i)
        mat1 = mat1 @ matr
    return matfin
expon(input(), input())
