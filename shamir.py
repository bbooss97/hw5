import random as r
import numpy as np
from decimal import *
from matplotlib import pyplot as plt
from numpy.polynomial.polynomial import Polynomial
getcontext().prec = 10**4
maxRandomCoefficients = 10**5


def drawFromCoefficients(coefficients):
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


def drawFromShards(shards,k):
    x=np.array([i[0]for i in shards ],dtype="float64")
    y=np.array([i[1]for i in shards],dtype="float64")

    coefficients=np.polynomial.Polynomial.fit(x, y, k)
    coefficients=[i.round(0) for i in coefficients]
    drawFromCoefficients(coefficients)


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
        drawFromCoefficients(coefficients)
    return shards


def findSecret(shards, k):
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
    s = 5423789
    draw = True
    shards = createShards(k, n, s, draw)
    print(findSecret(shards, k))
    drawFromShards(shards,k)
 

