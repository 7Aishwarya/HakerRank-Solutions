'''You’re given the pointer to the head nodes of two sorted linked lists. The data in both lists will be 
sorted in ascending order. Change the next pointers to obtain a single, merged linked list which also has 
data in ascending order. Either head pointer given may be null meaning that the corresponding list is empty.'''

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    node1 = head1
    node2 = head2
    newnode = None
    if not node1:
        return node2
    if not node2:
        return node1
    if node1 and node2:
        if node1.data <= node2.data:
            newnode = node1
            node1 = newnode.next
        else:
            newnode = node2
            node2 = newnode.next
        newhead = newnode
    while node1 and node2:
        if node1.data <= node2.data:
            newnode.next = node1
            newnode = node1
            node1 = newnode.next
        else:
            newnode.next = node2
            newnode = node2
            node2 = newnode.next
    if not node1:
        newnode.next = node2
    if not node2:
        newnode.next = node1
    return newhead


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
