'''Happy Ladybugs is a board game having the following properties:

The board is represented by a string, b, of length n. The  character of the string, b[i], denotes the ith cell of the board.
- If b[i] is an underscore (i.e., _), it means the ith cell of the board is empty.
- If b[i] is an uppercase English alphabetic letter (ascii[A-Z]), it means the ith cell contains a ladybug of color b[i].
- String b will not contain any other characters.
A ladybug is happy only when its left or right adjacent cell (i.e., b[i+1] or b[i-1]) is occupied by another ladybug having the same color.
In a single move, you can move a ladybug from its current position to any empty cell. 
Given the values of n and b for g games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For 
each game, print YES on a new line if all the ladybugs can be made happy through some number of moves. Otherwise, print NO. 
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    if b.count("_") == 0:
        for i in range(1,len(b)-1):
            if b[i]!=b[i+1] and b[i-1]!=b[i]:
                return "NO"
    for i in b:
        if i!="_" and b.count(i)==1:
            return "NO"
    
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

