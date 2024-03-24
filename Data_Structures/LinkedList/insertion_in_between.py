class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): 
        self.head = None
        
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end = " ")
            temp = temp.next
    
    def insertAtEnd(self, val):
        if self.head == None:
            # Inserting First Node in the Linked List
            self.head = Node(val)
        else:
            # Creating New Node
            newNode = Node(val)
            # Updating the `next` variable of newNode as head
            newNode.next = self.head
            # Creating a temp node to iterate over Linked List
            temp = self.head
            # Iterating till the `next` variable of temp is not equal to None
            while temp.next is not None:
                temp = temp.next
            # Temp is at tail of the Linked List
            temp.next = newNode;
            # Updating `next` variable of newNode as None
            newNode.next = None;
    def generateX(self,pos):
        # If the Linked List is empty return None
        if self.head == None:
            return self.head
        
        cnt = 1
        x = None
        temp = self.head
        while temp is not None:
            if cnt == pos:
                # If the count is equal to pos store the address of head and break the iteration
                x = temp
                break
            cnt+=1
            temp = temp.next
        return x


list = LinkedList()
list.insertAtEnd(1)
list.insertAtEnd(2)
list.insertAtEnd(3)
list.insertAtEnd(4)


# Creating New Node
newNode = Node(5);    
# Generating the Address of x'th Node
x = list.generateX(2);
# Storing the Address of y'th Node
y = x.next;

# Updating the `next` variable of x as newNode
x.next = newNode;
# Updating the `next` variable of newNode as y
newNode.next = y;

# Printing the Linked List
list.print()
