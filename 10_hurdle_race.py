#!/bin/python3

import math
import os
import random
import re
import sys

def hurdleRace(k, height):
    if max(height) - k < 0: result = 0
    elif max(height) - k >= 0: result = max(height) - k
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
