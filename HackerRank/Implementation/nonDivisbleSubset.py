#!/bin/python3

import os
import sys

#
# Complete the nonDivisibleSubset function below.
#
def nonDivisibleSubset(k, S):
    table=[0]*k
    for i in S:
        table[i%k]+=1
    s=min(table[0],1)
    for i in range(1,k//2+1):
        if (i!=k-i):
            s+=max(table[i],table[k-i])
    return s+1 if k%2==0 else s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
