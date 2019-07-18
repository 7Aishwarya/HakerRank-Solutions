'''You are given an array of n integers, ar=[ar[0],ar[1],...,ar[n-1]], and a positive integer, k. 
Find and print the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

For example, ar = [1,2,3,4,5,6] and k=5. Our three pairs meeting the criteria are [1,4], [2,3] and [4,6].
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    c = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if((ar[i]+ar[j])%k == 0):
                c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
