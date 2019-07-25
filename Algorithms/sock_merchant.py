#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    l = sorted(ar)
    total = 0
    i = 0
    while i!=(n-1):
        if l[i] == l[i+1]:
            total+=1
            i+=2
        else:
            i+=1
    return total


        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#this code do not pass all the test cases