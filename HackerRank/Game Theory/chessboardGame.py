#!/bin/python3

import sys

def chessboardGame(x, y):
    x=x%4
    y=y%4
    return "First" if((y==0)or (y==3)or (x==0)or(x==3))else "Second"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        result = chessboardGame(x, y)
        print(result)
