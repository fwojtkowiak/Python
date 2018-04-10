#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    arr.sort()
    smallest=abs(arr[1]-arr[0])
    for i in range(2,len(arr)):
        if(abs(arr[i]-arr[i-1])<=smallest):
            smallest=abs(arr[i]-arr[i-1])
    return smallest
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
