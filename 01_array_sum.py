#!/bin/python3

import math
import os
import random
import re
import sys

def control(arr):
    y = []
    for i in range(arr):
        y.append(int(input()))
    sum1 = sum(y)
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

