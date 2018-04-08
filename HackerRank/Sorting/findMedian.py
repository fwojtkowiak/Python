#!/bin/python3

import sys

def findMedian(arr):
    arr.sort()
    n=len(arr)
    if(n%2==0):
        return (arr[n-1]+arr[n])/2
    else:
        return arr[int(n/2)]
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)
