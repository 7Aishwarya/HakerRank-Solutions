'''Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 
2 space-separated strings on a single line (see the Sample below for more detail).

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s=[]
for i in range(n):
    s.append(input())
for i in s:
    for j in range(0,len(i),2):
        print(i[j],end = "")
    print(" ", end = "")
    for j in range(1,len(i),2):
        print(i[j],end = "")
    print()


