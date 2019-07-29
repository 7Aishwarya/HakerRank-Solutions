'''Read an integer n and then print n natural numbers.
Sample Input 
5
Sample Output 
12345
'''


if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1,1):
        print(i, end = '')

