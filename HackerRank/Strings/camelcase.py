#!/bin/python3

import sys

def camelcase(s):
    return sum(1 for i in s if ord(i)>=60 and ord(i)<=90)+1
if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
