#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):    
    n=len(arr)
    print ("{:6.6f}".format(len([x for x in arr if x > 0])/n))
    print ("{:6.6f}".format(len([x for x in arr if x < 0])/n))
    print ("{:6.6f}".format(len([x for x in arr if x == 0])/n))



#if __name__ == '__main__':
    #n = int(input())

#arr = list(map(int, input().rstrip().split()))
arr=[-4,0,0,0,1,1]
plusMinus(arr)
