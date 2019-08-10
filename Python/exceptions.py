'''You are given two values a and b. 
Perform integer division and print a/b.

Input Format
The first line contains T, the number of test cases. 
The next T lines each contain the space separated values of a and b.

Output Format
Print the value of a/b. 
In the case of ZeroDivisionError or ValueError, print the error code.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    a,b=input().split()
    try:
        c = int(a)//int(b)
        print(c) 
    except Exception as e:
        print("Error Code:",e)

