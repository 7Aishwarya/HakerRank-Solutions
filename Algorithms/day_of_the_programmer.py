#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if 1700<=year<=1917:
        if year%4==0:
            s='12.09.'+str(year)
        else:
            s='13.09.'+str(year)
    if 1919<=year<=2700:
        if year%400==0 or (year%4==0 and year%100!=0):
            s='12.09.'+str(year)
        else:
            s='13.09.'+str(year)
    if year == 1918:
        s='26.09.1918'

    return s
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
