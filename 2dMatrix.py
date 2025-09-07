#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    
    fDiagonal=0
    sDiagonal=0
    
    for i in range(n):
        fDiagonal+= arr[i][i]
        sDiagonal += arr[i][n-1-i]
    return abs(fDiagonal-sDiagonal)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    
    print(result)
