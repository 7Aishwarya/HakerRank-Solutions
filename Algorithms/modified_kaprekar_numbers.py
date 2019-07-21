'''A modified Kaprekar number is a positive whole number with a special property. If you square it, 
then split the number into two integers and sum those integers, you have the same value you started with.

Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2*d digits long or 
(2*d)-1 digits long. Split the string representation of the square into two parts, l and r. The right hand part, r must 
be d digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see 
if you get n.
For example, if n=5, d=1 then n^2=25. We split that into two strings and convert them back to integers 2 and 5. We test 
2+5=7!=5, so this is not a modified Kaprekar number. If n=9, still d=1, and n^2=81. This gives us 1+8=9, the original n.
Note: r may have leading zeros.

Given two positive integers p and q where p is lower than q, write a program to print the modified Kaprekar numbers in 
the range between p and q, inclusive.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    c=0
    for i in range(p,q+1):
        sq=i*i
        d=len(str(i))
        length= len(str(sq))
        square = str(sq)
        if(length==(2*d)):
            first=square[:d]
            second=square[d:]
            if((int(first)+int(second))==i):
                print(i,end=' ')
                c=c+1
        if(length==((2*d)-1) and length>d):
            first=square[:d-1]
            second=square[d-1:]
            if((int(first)+int(second))==i):
                print(i,end=' ')
                c=c+1
        if(length==d):
            first=sq
            if(first==i):
                print(i,end=' ')
                c=c+1
    if(c==0):
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
