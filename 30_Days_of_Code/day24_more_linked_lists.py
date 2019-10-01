'''Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.'''



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        node = head
        l = []
        while node!=None:
            l.append(node.data)
            node = node.next
        l.sort()
        newnode = head
        i = 0
        while node!=None:
            node.data = l[i]
            node = node.next
        node = head
        while node.next:
            if node.data == node.next.data:
                node.next = node.next.next
            else:
                node = node.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 