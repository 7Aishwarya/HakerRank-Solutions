'''Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to N-1 (both inclusive). 
You have two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol that particular 
petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. 
Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop 
at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.

Input Format
The first line will contain the value of N.
The next N lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump and the next petrol pump.

Output Format
An integer which will be the smallest index of the petrol pump from which we can start the tour.

Sample Input
3
1 5
10 3
3 4
Sample Output
1
'''


#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    p = 0
    n = 0
    temp = 0
    i =  0
    while(i != (len(petrolpumps)-1)):
        if i == 0:
            p = p + petrolpumps[i][0]
            n = n + petrolpumps[i][1]
            i+=1

        if p > n:
            p = p + petrolpumps[i][0]
            n = n + petrolpumps[i][1]
            i+=1
        else:
            temp+=1
            i = temp
            p = petrolpumps[temp][0]
            n = petrolpumps[temp][1]
            
    return temp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
