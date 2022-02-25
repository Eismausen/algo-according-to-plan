#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    path_list = list(path)
    if steps > 100000:
        return 0
    elevation = 0
    valleys = 0
    while len(path_list) > 0:
        #step
        step = path_list.pop(0)
        if (step == 'D'):
            elevation -= 1
        else:
            elevation += 1
        if (elevation < 0):
            while (elevation < 0) & (len(path_list) > 0):
                step = path_list.pop(0)
                if (step == 'D'):
                    elevation -= 1
                else:
                    elevation += 1
            valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
