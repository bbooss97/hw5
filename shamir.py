import random as r
import numpy as np
from matplotlib import pyplot as plt
def createShards(k,n,s):
    coefficients=[r.randint(0,10000000) for i in range(k)]
    coefficients[0]=s
    shards=[]
    for i in range(n):
        y=0
        x=r.randint(0,10000000)
        for j in range(k):
            y+=x**j*coefficients[j]
        shards.append((x,y))
    return shards
def findSecret(shards,k):
    if len(shards)<k:
        print("you need more shards")
        return -1
    a=[[0 for j in range(k)] for i in range(k)]
    b=[0 for i in range(k)]
    for i in range(k):
        x=shards[i][0]
        y=shards[i][1]
        b[i]=y
        for j in range(k):
            a[i][j]=x**j
    a=np.asarray(a)
    b=np.asarray(b)
    return np.linalg.solve(a,b)

if __name__ == "__main__":
    shards=createShards(10,1000,3421)
    print(findSecret(shards,10))

