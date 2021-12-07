import random as r
import numpy as np
from decimal import *
from matplotlib import pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
getcontext().prec = 10**4
maxRandomCoefficients = 10**5


def drawFunction(coefficients):
    size = 10000
    x = np.linspace(-size, size,10000)

    y=[]
    for i in range(len(x)):
        sum=0
        for j in range(len(coefficients)):
            sum+=(x[i]**j)*coefficients[j]
        y.append(sum)
    plt.plot(x, y)
    plt.grid()
    plt.axhline(color='r')
    plt.axvline( color='r')
    plt.show()


def createShards(k, n, s, draw):
    g=0
    coefficients =[r.randint(0, maxRandomCoefficients) for i in range(k)]
    coefficients[0] = s
    print("those are the coefficients from 0 to k-1")
    print(coefficients)
    shards = []
    for i in range(n):
        y = 0
        l=[i[0] for i in shards]
        x=0
        while(True):
            x = r.randint(0, maxRandomCoefficients)
            if x not in l:
                break
        for j in range(k):
            y += (x**j)*coefficients[j]
        shards.append((x, y))
    print("shards are generated")
    if draw == True:
        drawFunction(coefficients)
    return shards


def findSecrett(shards, k):
    if len(shards) < k:
        print("you need more shards")
        return -1
    secret = Decimal(0)
    for i in range(k):
        li = Decimal(1)
        xi = shards[i][0]
        yi = shards[i][1]
        for j in range(k):
            xj = shards[j][0]
            if i == j:
                continue
            li *= -Decimal(Decimal(xj)/(xi-xj))
        secret += Decimal(yi*li)
    return round(Decimal(secret))


if __name__ == "__main__":
    k = 5
    n = 10
    s = 542389543789
    draw = True
    shards = createShards(k, n, s, draw)
    print(findSecrett(shards, k))


# def findSecret(shards,k):
#     if len(shards)<k:
#         print("you need more shards")
#         return -1
#     a=[[0 for j in range(k)] for i in range(k)]
#     b=[0 for i in range(k)]
#     for i in range(k):
#         x=shards[i][0]
#         y=shards[i][1]
#         b[i]=y
#         for j in range(k):
#             a[i][j]=x**j
#     a=[[Decimal(i) for i in a[j]]for j in range(k)]
#     b=[Decimal(i) for i in b]

#     a=np.asarray(a)
#     b=np.asarray(b)
#     return np.linalg.solve(a,b)
