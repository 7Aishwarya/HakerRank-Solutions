#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maximum=-63
    for i in range(0,4,1):
        for j in range(0,4,1):
            sum1 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if(sum1>maximum):
                maximum = sum1 
    print(maximum)
