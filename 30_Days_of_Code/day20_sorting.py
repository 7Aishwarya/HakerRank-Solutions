'''Bubble Sort'''


#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numswaps = 0
for i in range(0,n-1,1):
    for j in range(0,n-1,1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numswaps = numswaps + 1
print("Array is sorted in", numswaps, "swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])


