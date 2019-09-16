'''Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.'''


#!/bin/python3

import sys


S = input().strip()
try:
    a = int(S)
    print(a)
except:
    print("Bad String")


