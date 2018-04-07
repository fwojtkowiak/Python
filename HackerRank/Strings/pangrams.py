#!/bin/python3

import os
import sys
from string import ascii_lowercase

#
# Complete the pangrams function below.
#
def pangrams(s):
    s2=s.lower()
    res="pangram" if sum(1 for c in ascii_lowercase if c in s2)==26 else "not pangram"          
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
