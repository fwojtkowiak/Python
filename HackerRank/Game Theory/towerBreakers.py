#!/bin/python3

import sys

def towerBreakers(n, m):
    return 2 if (m==1 or n%2==0) else 1

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        result = towerBreakers(n, m)
        print(result)
