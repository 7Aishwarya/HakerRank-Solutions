# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
n = int(input())
d = {}
for i in range(n):
    name, phone = input().split()
    d[name] = phone
while True:
    try:
        input_name = input()
        c = d.get(input_name)
        if c == None:
            print("Not found")
        else:
            print(input_name, end = "")
            print("=", end = "")
            print(c)
    except EOFError:
        break 




