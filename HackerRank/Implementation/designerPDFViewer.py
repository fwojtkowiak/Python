#!/bin/python3

import sys
from string import ascii_lowercase

def designerPdfViewer(h, word):
    return(max(h[ord(i)-97] for i in word)*len(word))