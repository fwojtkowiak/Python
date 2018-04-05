#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    a=0
    b=0
    c=0
    for i in arr:
        if(i>0):
            a+=1
        elif(i<0):
            b+=1
        else:
            c+=1
    print (a/(a+b+c),b/(a+b+c),c/(a+b+c))

#if __name__ == '__main__':
    #n = int(input())

#arr = list(map(int, input().rstrip().split()))
arr=[-4,0,0,0,1,1]
plusMinus(arr)
