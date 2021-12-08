#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    just_one = list(set(ar)) # unique ar numbers
    count = 0
    for i in just_one:
        if ar.count(i) // 2 >= 1 :
            count += ar.count(i) // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
