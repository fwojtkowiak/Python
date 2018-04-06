#!/bin/python3

import sys

def hurdleRace(k, height):
    result = max(max(i for i in height)-k,0)
    return result