'''Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer 
denoting the maximum number of consecutive 1's in n's binary representation.'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    l = []
    while n!=1:
        s = str(n%2)
        l.append(s)
        n = n//2
    l.append("1")
    c = 0
    maximum = 0
    if l[0] == "1":
        c = 1
        maximum = 1
    for i in range(1,len(l)):
        if l[i] == "1":
            c = c + 1
            if c > maximum:
                maximum = c
        if l[i] != "1":
            c = 0
    print(maximum)






