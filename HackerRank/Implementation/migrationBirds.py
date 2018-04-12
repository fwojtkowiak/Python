#!/bin/python3

import sys

def migratoryBirds(n, ar):
    m=max(ar)
    res=[0]*(m+1)
    for i in range(m+1):
        res[i]=ar.count(i)
    return res.index(max(res))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
