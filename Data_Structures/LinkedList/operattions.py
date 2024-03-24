class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_Data = Node(data)
            new_Data.next = self.head
            self.head = new_Data

    def rotate(self,k):
        if k == 0:
            return

        count = 1

        cur = self.head

        while cur:
            if count == k:
                break
            cur = cur.next
            count += 1
        
        kthNode = cur

        while cur.next != None:
            cur = cur.next
        
        cur.next = self.head
        self.head = kthNode.next
        kthNode.next = None
        
            

    
    # to search an element in linkedlist
    def search(self, data):
        cur_data = self.head

        while cur_data != None:
            if cur_data.data == data:
                return True
            cur_data = cur_data.next
        return False
    
    #printing an element in linkedlist
    def print(self):
        cur_data = self.head

        while cur_data != None:
            print(cur_data.data, end = "-->")
            cur_data = cur_data.next
        print()

    # find length of linkedlist
    def length(self):
        cur_data = self.head
        count = 0

        while cur_data != None:
            count += 1
            cur_data = cur_data.next
        return count
    
    def reverse(self):
        pre = None
        cur_data = self.head

        while cur_data != None:
            next = cur_data.next
            cur_data.next = pre
            pre = cur_data
            cur_data = next
        self.head = pre
    
    
if __name__ == "__main__":

    ls = LinkedList()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    ls.push(40)
    ls.push(50)

    ls.print()

    ls.rotate(3)
    ls.print()

    ls.print()

    find = ls.search(20)
    print(find)

    find2 = ls.search(60)
    print(find2)

    size = ls.length()
    print(size)

    ls.reverse()
    ls.print()

    