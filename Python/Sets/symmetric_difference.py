'''Given  sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
l1 = input().split()
set1 = set()
for i in l1:
    set1.add(int(i))
b = int(input())
l2 = input().split()
set2 = set()
for i in l2:
    set2.add(int(i))
x = set1.difference(set2)
y = set2.difference(set1)
z = x.union(y)
l = []
for i in z:
    l.append(i)
l.sort()
for i in l:
    print(i)







