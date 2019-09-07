'''Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1<=i<=10) should be printed on a new line 
in the form: n x i = result.'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for i in range(10):
        print(n,"x",i+1,"=",n*(i+1))
