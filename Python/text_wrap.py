'''You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.
Input Format
The first line contains a string, S. 
The second line contains the width, w.

Sample Input
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''


import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    s = wrapper.fill(text=string) 
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)