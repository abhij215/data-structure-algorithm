
"""creating a class node to initiate the node which contain the data and the next 
    element pointer"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:
    
    def __int__(self):
        self.head = None
    
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            cur = self.head

            while cur.next != None:
                cur = cur.next
            
            cur.next = newNode
            newNode.next = None
    
    def printList(self):
        cur = self.head

        while cur!= None:
            print(cur.data, end = "-->")
            cur = cur.next
        
        print()

if __name__ == '__main__':
    pass