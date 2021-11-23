#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    y = [12,13,14,15,16,17,18,19,20,21,22,23,24]

    if s[-2:] == "PM":
        if int(s[0:2]) not in y: s= str(int(s[0:2]) + 12) + s[2:8]
        else: s = s[:8]
    if s[-2:] == "AM":
        if int(s[0:2]) in y: s = str(int(s[0:2]) - 12) + s[2:8]
        else: s = s[:8]
    if s[1] == ":": s = "0" + s
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
