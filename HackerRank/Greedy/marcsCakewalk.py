#!/bin/python3

import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    return (sum(2**i*calorie[i] for i in range(len(calorie))))
if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)
