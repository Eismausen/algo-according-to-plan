#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    # if we know the frequency of a's in the string (a_count), we can
    # multiply that frequency by the number of occurrences of the
    # entire string that are possible for a sequence of length
    # n (n // s_length)
    s_length = len(s)
    s_list = list(s)
    a_count = s_list.count('a')
    approx_a_count = a_count * (n // s_length)
    remainder = n % s_length
    remainder_count = s_list[:remainder].count('a')
    return approx_a_count + remainder_count
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
