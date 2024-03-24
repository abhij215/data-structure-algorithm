class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            cur = self.head

            while cur.next:
                cur = cur.next

            cur.next = newNode
            newNode.next = None
    
    def printlist(self):
        cur = self.head
        if cur != None:
            while cur:
                print(cur.data, end = "-->")
                cur = cur.next
        else:
            print("not present")

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.mergeSort(left)
        right = self.mergeSort(right)

        res = self.mergeList(left, right)

    def getMid(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def mergeList(self, list1, list2):
        tail = dummy = Node(0)

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
    

if __name__ == "__main__":
    ls = LinkedList()
    ls.push(23)
    ls.push(12)
    ls.push(34)
    ls.push(7)
    ls.push(23)
    ls.push(24)
    ls.push(1)

    ls.printlist()

    ls.head = ls.mergeList(ls.head)

    ls.head.printlist()



