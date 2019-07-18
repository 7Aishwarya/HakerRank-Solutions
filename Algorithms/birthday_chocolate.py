'''Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. 
She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month 
and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, s=[2,2,1,3,2]. She wants to find segments summing to Ron's birth day, d=4
with a length equalling his birth month, m=2. In this case, there are two segments meeting her criteria: [2,2] and [1,3].
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    c=0
    for i in s:
        c+=1
    total = 0
    for i in range(c):
        sum1 = sum(s[i:i+m])
        if sum1 == d:
            total +=1
    return total


      


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
