class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def swapNode(self,x,y):
        
        if x ==y:
            return
        
        preX = None
        curX = self.head
        while curX!= None:
            if curX.data == x:
                break
            preX = curX
            curX = curX.next
        
        preY = None
        curY = self.head
        while curY != None:
            if curY.data == y:
                break
            preY = curY
            curY = curY.next
        
             
        if preX != None:
            preX.next = curY
        else:
            self.head = curY

        if preY != None:
            preY.next = curX
        else:
            self.head = curX

        if curX == None or curY == None:
            return
        
        temp = curX.next
        curX.next = curY.next
        curY.next = temp


    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)

            cur = self.head

            while cur.next!=None:
                cur = cur.next

            cur.next = newNode
            newNode.next = None

    def printlist(self):
        cur = self.head

        while cur!= None:
            print(cur.data, end = "-->")
            cur = cur.next
        
        print()


if __name__ == "__main__":

    ls = LinkedList()

    ls.push(10)
    ls.push(15)
    ls.push(20)
    ls.push(25)
    ls.push(30)
    ls.push(40)
    ls.push(41)
    ls.push(47)

    ls.printlist()


    ls.swapNode(15,30)

    ls.printlist()