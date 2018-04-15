#!/bin/python3

import sys

def sockMerchant(n, ar):
    r=0
    for a in set(ar):
        r+=ar.count(a)//2
    return r
    
    
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
