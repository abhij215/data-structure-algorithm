class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def insertAtBegining(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    
    def insertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            new_data = Node(data)
            new_data.next = self.head
            temp = self.head

            while temp.next != None:
                temp = temp.next
            
            temp.next = new_data
            new_data.next = None
    
    def num(self, index):
        cur = self.head
        count = 0

        while cur != None:
            if count == index:
                return cur.data
            count += 1
            cur = cur.next

    def index(self, data):
        cur = self.head
        count = 0

        while cur != None:
            if cur.data == data:
                return count
            count += 1
            cur = cur.next
    

    def printlist(self):
        temp = self.head
        if temp != None:
            while temp != None:
                print(temp.data, end = "-->")
                temp = temp.next
        else:
            print("not present")
        print()

    def insertarray(self, arr):
        self.head = None
        for i in arr:
            self.insertAtBegining(i)


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.insertAtBegining(10)
    mylist.insertAtBegining(13)
    mylist.printlist()

    arrayList = LinkedList()

    arr = [1,23,34,5,66,3,4,8,89]
    arrayList.insertarray(arr)
    arrayList.printlist()

    newlist = LinkedList()
    newlist.insertAtEnd(10)
    newlist.insertAtEnd(20)

    newlist.printlist()


    
    
    
    
