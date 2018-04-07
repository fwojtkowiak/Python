#!/bin/python3

import sys

def funnyString(s):
    n=len(s)
    res=("Funny" if sum(1 for i in range(1,n) if abs(ord(s[i])-ord(s[i-1]))==abs(ord(s[-i])-ord(s[-i-1])))==n-1 else "Not Funny")    
    return res

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
