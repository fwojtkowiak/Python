#!/bin/python3

import sys
from itertools import repeat

def missingNumbers(arr, brr):
    a=[0]*(max(brr)+1)
    res=[]
    for i in arr:
        a[i]-=1
    for i in brr:
        a[i]+=1
    for i in range(0,max(brr)+1):
        if (a[i]>0):
            res.append(i)
    return res
                       
                       
                       
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))


