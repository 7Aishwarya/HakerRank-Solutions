'''Two cats and a mouse are at various positions on a line. You will be given their starting positions. 
Your task is to determine which cat will reach the mouse first, assuming the mouse doesn't move and 
the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to 
move and it will escape while they fight.
You are given q queries in the form of x, y, and z representing the respective positions for cats A and B, 
and for mouse C. 

Sample Input 
2
1 2 3
1 3 2
Sample Output 
Cat B
Mouse C
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(x-z)<abs(y-z):
        ans = "Cat A"
    if abs(y-z)<abs(x-z):
        ans = "Cat B"
    if abs(x-z)==abs(y-z):
        ans = "Mouse C"
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
