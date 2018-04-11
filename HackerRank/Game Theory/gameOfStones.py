#!/bin/python3

import sys

def gameOfStones(n):
    return "Second" if (n%7 in [0,1]) else "First"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        print(result)
