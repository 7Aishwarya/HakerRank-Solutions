'''You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=list(s)
    n = ""
    for i in range(len(l)):
        if l[i]==" ":
            l[i+1] = l[i+1].upper()
        if i == 0:
            l[i] = l[i].upper()
        n+=l[i]
    return n
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
