#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # length = len(a)
    # b = list(range(length))
    # # print("a[0]",a[0])
    # for i in range(length-1,-1,-1):
    #     diff = i-d
    #     if(diff<0):
    #         b[length+(diff)] = a[i]
    #     else:
    #         b[diff] = a[i]
    # return b
    i = d% len(a)
    return(a[i:] + a[:i])




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()

    # I/P 5 4
    # 1 2 3 4 5
