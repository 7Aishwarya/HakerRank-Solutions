'''You are given a pointer to the root of a binary tree. Print the top view of the binary tree. 
For example :

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top View : 1 -> 2 -> 5 -> 6
'''


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    if root:
        node = root
        q = [node]
        node.level = 0
        d = {}
        d[0] = node.info
        while len(q)>0:
            node = q.pop(0)
            if node.left is not None:
                node.left.level = node.level - 1
                if node.left.level not in d:
                    d[node.left.level] = node.left.info
                q.append(node.left)      
            if node.right is not None:
                node.right.level = node.level + 1
                if node.right.level not in d:
                    d[node.right.level] = node.right.info
                q.append(node.right)
        for i in sorted(d):
            print(d[i], end = " ")






tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)