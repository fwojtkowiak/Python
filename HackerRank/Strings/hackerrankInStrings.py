#!/bin/python3

import sys

def hackerrankInString(s):
    h="hackerrank"
    s2=[x for x in s]
    res=0
    for a in h:
        if (a in s2):
            s2=s2[ ((next(i for i in range(len(s2)) if a==s2[i]))+1):]
            res+=1          
    return "YES" if res==len(h) else "NO"
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
