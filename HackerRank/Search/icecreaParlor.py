#!/bin/python3

import sys

def icecreamParlor(m, arr):
    res=[]
    for i in range(0,len(arr)):
        if (m-arr[i]) in arr[i+1:len(arr)]:
            arr1=arr[i+1:len(arr)]
            x=arr1.index(m-arr[i])
            res.append(i+1)
            res.append(i+x+2)
    return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))


