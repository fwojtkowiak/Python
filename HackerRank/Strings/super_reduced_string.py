#!/bin/python3

import sys

def super_reduced_string(s):
    result = []
    for a in s:
        if result and result[-1]==a:
            result.pop()
        else:
            result.append(a)
    result=''.join(result)
    return result or "Empty String"
s = input().strip()
result = super_reduced_string(s)
print(result)
