class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            cur = self.head

            while cur.next != None:
                cur = cur.next

            cur.next = newNode
            newNode.next = None
    
    def print(self):
        cur = self.head

        if cur != None:
            while cur != None:
                print(cur.data, end = "-->")
                cur = cur.next
        else:
            print("not present")
        print()

    def mergeList(self, headA, headB):
        dummyNode = Node(0)
        tail = dummyNode

        while True:

            if headA is None:
                tail.next = headB
                break
            if headB is None:
                tail.next = headA
                break

            if headA.data <= headB.data:
                tail.next = headA
                headA = headA.next
            else:
                tail.next = headB
                headB = headB.next

            tail = tail.next
        
        return dummyNode.next


if __name__ == "__main__":
    ls = LinkedList()
    ls.push(10)
    ls.push(29)
    ls.push(31)
    ls.push(33)
    ls.push(39)
    ls.push(41)

    ls.print()

    ls2 = LinkedList()

    ls2.push(5)
    ls2.push(15)
    ls2.push(30)
    ls2.push(32)
    ls2.push(37)
    ls2.push(41)
    
    ls.head = ls.mergeList(ls.head, ls2.head)

    
    ls.print()
        