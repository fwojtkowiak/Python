#!/bin/python3

import sys

def solve(n, s, d, m):
    r=0
    for i in range(n-m+1):
        if sum(s[j] for j in range (i,i+m))==d :
            r+=1
    return r
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
