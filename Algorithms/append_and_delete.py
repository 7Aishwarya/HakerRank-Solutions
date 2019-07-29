'''You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Sample Input 
hackerhappy
hackerrank
9
Sample Output 
Yes
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    notsame = 0
    same = 0
    for i in s:
        if(t.find(i)!=-1):
            same+=1
        else:
            break

    l1 = len(t) - same      
    l2 = len(s) - same
    total = l1 + l2
    if total<=k:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()


#this code do not pass all the test cases



