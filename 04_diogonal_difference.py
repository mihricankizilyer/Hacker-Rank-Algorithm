#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    k = 0
    m = 0
    for i in range(len(arr)):
        k += arr[i][i]
        m += arr[i][-i - 1]
        result = abs(k - m)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
