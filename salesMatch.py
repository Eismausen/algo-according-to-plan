#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # basic histogram solution:
    # for each element of ar, create a k,v pair in your "sock drawer"
    # then hit each v of the k,v with a //2 and sum
    sock_drawer = {}
    for sock in ar:
        if sock in sock_drawer:
            sock_drawer[sock] += 1
        else:
            sock_drawer[sock] = 1
    paired_socks = 0
    for color, socks in sock_drawer.items():
        if (socks >= 2):
            paired_socks += socks // 2
    return paired_socks
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
