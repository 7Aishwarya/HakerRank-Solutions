'''Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    for i in arr:
        print(i, end = " ")
