class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        return True if self.head is None else False
    
    def push(self,data):
        if self.head == None:
            self.head = Node(data)

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.isempty():
            return None
        else:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped

    def peek(self):
        cur = self.head
        if self.head == None:
            return None
        else:
            return cur.data
        
    
    def display(self):
        cur = self.head

        if self.isempty():
            return None
        
        else:

            while cur != None:
                print(cur.data, end = "-->")
                cur = cur.next
            
                


if __name__ == "__main__":
    st = Stack()

    st.push(10)
    st.push(12)
    st.push(13)
    st.push(15)
    st.push(98)

    st.display()

    print()

    print(st.isempty())

    st.pop()
    st.pop()
    st.display()

    print()

    print(st.peek())