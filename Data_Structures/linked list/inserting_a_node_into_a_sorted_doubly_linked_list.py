'''Given a reference to the head of a doubly-linked list and an integer, data, create a new 
DoublyLinkedListNode object having data value data and insert it into a sorted linked list while 
maintaining the sort.'''


#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    newnode = DoublyLinkedListNode(data)
    node = head
    if node.data>data:
        node.prev = newnode
        newnode.next = node
        head = newnode
    else:
        y = 0
        while node is not None:
            if node.data>data:
                y = 1
            node = node.next
        if y == 0:
            node = head 
            while node.next:
                node = node.next
            node.next = newnode
            newnode.prev = node 
        else:
            node = head
            while node.data<=data:
                temp = node
                node = node.next
            temp.next = newnode 
            newnode.next = node
            node.prev = newnode
            newnode.prev = temp
    return head



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
