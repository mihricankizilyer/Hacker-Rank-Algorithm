#!/bin/python3

import math
import os
import random
import re
import sys

max_sum = []
min_sum = []


def miniMaxSum(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            max_sum.append(arr[i + 1])
            min_sum.append(arr[i])

    min_result = sum(min_sum)
    max_result = sum(max_sum)

    print(min_result, max_result)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
