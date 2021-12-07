#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    res1 = [m for m in range(i, j + 1)] # normal numbers
    res2 = [int(str(i)[::-1]) for i in range(i, j + 1)] # reversed numbers 

    res3 = 0
    for s in range(len(res1)):
        if ((res1[s] - res2[s]) / k) == ((res1[s] - res2[s]) // k):
            res3 += 1

    return res3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    i = int(first_multiple_input[0])
    j = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    result = beautifulDays(i, j, k)
    fptr.write(str(result) + '\n')
    fptr.close()
