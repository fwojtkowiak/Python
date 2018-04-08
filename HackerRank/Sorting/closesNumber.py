#!/bin/python3

import sys

def closestNumbers(arr):
    arr.sort()
    min_v=min(abs(arr[i]-arr[i-1]) for i in range (1,len(arr)))
    res=[]
    for i in range(1,len(arr)):
        if abs(arr[i]-arr[i-1])==min_v:
            res.append(i-1)
            res.append(i)
    return (arr[k] for k in res)
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))


5