'''Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there. 
It must return an integer array containing the numbers of times she broke her records.

Sample Input 
9
10 5 20 20 4 5 2 25 1
Sample Output 
2 4
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maximum = scores[0]
    minimum = scores[0]
    c = 0
    d = 0
    for i in scores:
        if i > maximum:
            maximum = i
            c+=1
        if i < minimum:
            minimum = i
            d+=1
    l = [c,d]
    return l
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
