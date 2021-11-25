#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    sum1 = []
    result = []
    m = 0

    for i in ar:
        m = m + 1
        for s in ar[m:]:
            if i != s:
                sum1.append(i + s)
            else:
                pass
    for c in sum1:
        if c % k == 0: result.append(c)
    return len(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
