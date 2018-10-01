# https://www.hackerrank.com/challenges/runningtime/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    length = len(arr)
    count = 0
    for i in range(1,length):
        for j in range(0,i):
            if(arr[i]< arr[j]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                count +=1
        print(arr)
    return count

if __name__ == '__main__':
    n = 4

    arr = [4,4,3,4]

    result = runningTime(arr)

    print(result)
