#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    poz = []
    neg = []
    zero = []
    div = len(arr)

    for i in arr:
        if i > 0:
            poz.append(i)
        elif i < 0:
            neg.append(i)
        elif i == 0:
            zero.append(i)

    poz_res = round(len(poz) / div, 6)
    neg_res = round(len(neg) / div, 6)
    zero_res = round(len(zero) / div, 6)

    print(poz_res)
    print(neg_res)
    print(zero_res)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
