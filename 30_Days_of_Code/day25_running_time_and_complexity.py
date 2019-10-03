'''Given a number, n find if it is prime or not.
Input Format
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.
Constraints
1<=T<=30
1<=n<=2*10^9
Output Format
For each test case, print whether n is Prime or Not Prime on a new line.'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())
for i in range(n):
    num = int(input()) 
    sqrt = int(math.sqrt(num)) 
    if num > 1:  
        for i in range(2,sqrt+1):  
            if (num % i) == 0:  
                print("Not prime")  
                break  
        else:  
            print("Prime")  

    else:  
        print("Not prime")  
