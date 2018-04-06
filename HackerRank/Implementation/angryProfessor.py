#!/bin/python3

import sys

def angryProfessor(k, a):
    can=sum(1 if i<=0 else 0 for i in a)
    if (can>=k):
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
