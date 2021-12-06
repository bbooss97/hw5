import random as r
import numpy as np
from decimal import *
from matplotlib import pyplot as plt
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
getcontext().prec=10000
maxRandomCoefficients =1000000


def drawFunction(coefficients):
    size=1**100
    x=np.linspace(-size,size)
    y=[]
    for i in range(len(x)):
        yy=0
        for j in range(len(coefficients)):
            yy+=(x[i]**j)*coefficients[j]
        y.append(yy)
    plt.plot(x,y)
    plt.grid()
    plt.show()

def createShards(k,n,s,draw):
    coefficients=[r.randint(0,maxRandomCoefficients) for i in range(k)]
    coefficients[0]=s
    shards=[]
    
    for i in range(n):
        y=0
        x=r.randint(0,maxRandomCoefficients)
        for j in range(k):
            y+=(x**j)*coefficients[j]
        shards.append((x,y))
    if draw==True:
        drawFunction(coefficients)
        

    return shards



def findSecrett(shards,k):
    if len(shards)<k:
        print("you need more shards")
        return -1
    secret=Decimal(0)
    for i in range(k):
        li=Decimal(1)
        xi=shards[i][0]
        yi=shards[i][1]
        for j in range(k):
            xj=shards[j][0]
            if i==j:
                continue
            li*= -Decimal(Decimal(xj)/(xi-xj))
        secret+=Decimal(yi*li)
    return round(Decimal(secret))


def getSecret(shards,k):
    a=[Decimal(x[0]) for i,x in enumerate(shards) if i<=k]
    b=[Decimal(y[1]) for i,y in enumerate(shards) if i<=k]

    return lagrange(a,b)
    return Polynomial(lagrange(a,b)).coef
    # return np.linalg.solve(a,b)

if __name__ == "__main__":
    k=5
    n=1000
    s=3471
    draw=True
    shards=createShards(k,n,s,draw)
    print(findSecrett(shards,k))












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