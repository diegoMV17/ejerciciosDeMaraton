import math
import os
import random
import re
import sys

def decentNumber(n):
    result = -1
    
    for i in range(n, -1, -1):
        if i % 3 == 0 and (n - i) % 5 == 0:
            result = '5' * i + '3' * (n - i)
            break
    print(result)
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        decentNumber(n)