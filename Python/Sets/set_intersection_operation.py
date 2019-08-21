'''The students of District College have subscriptions to English and French newspapers. Some students have 
subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has 
subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format

The first line contains n, the number of students who have subscribed to the English newspaper. 
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper. 
The fourth line contains b space separated roll numbers of those students.

Output Format
Output the total number of students who have subscriptions to both English and French newspapers.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
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
z = set1.intersection(set2)
count = z.__len__()
print(count)


