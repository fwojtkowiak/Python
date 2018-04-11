#!/bin/python3

import sys

def lonelyinteger(a):
    for i in set(a):
        if(a.count(i)==1):
            res=i
    return res

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
