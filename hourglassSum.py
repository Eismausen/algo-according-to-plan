#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    #hourglass_index = [0,0]
    glass_sums = []
    for i in range(0, len(arr)-2, 1):
        for j in range(0, len(arr[0])-2, 1):
            #print(f"Hourglass index: {i, j}")
            row1 = sum(arr[i][j:j+3])
            #print(f"row1 sum: {row1}")
            row2 = arr[i+1][j+1]
            #print(f"row2 sum: {row2}")
            row3 = sum(arr[i+2][j:j+3])
            #print(f"row3 sum: {row3}")
            temp_sum = sum([row1, row2, row3])
            print(f"temp_sum: {temp_sum}")
            glass_sums.append(temp_sum)
    
    print(f"glass sums: {glass_sums}")
    return max(glass_sums)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
