class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __int__(self):
        self.head = None

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            cur_data = self.head

            while cur_data.next != None:
                cur_data = cur_data.next
            
            cur_data.next = newNode
            newNode.next = None
    
    def insertAtStart(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            cur_data = self.head
            self.head = newNode
            newNode.next = cur_data
    
    def insertInBetween(self,after,data):
        newNode = Node(data)
        cur_data = self.head
        x = None

        while cur_data:
            if cur_data.data == after:
                x = cur_data
                break
            cur_data = cur_data.next
        
        y = x.next
        x.next = newNode
        newNode.next = y
    
    def deletionAtIndex(self,data):
        cur_data = self.head

        if cur_data!= None:
            if cur_data.data == data:
                self.head = cur_data.next
                cur_data = None
                return
        
        while cur_data!= None:
            if cur_data.data == data:
                break
            pre = cur_data
            cur_data = cur_data.next
        
        if cur_data is None:
            return
        
        pre.next = cur_data.next
        cur_data = None

        


            