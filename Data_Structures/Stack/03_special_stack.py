class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.Max = 100
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.Max-1:
            return True
        else:
            return False

    def push(self,x):
        if self.isFull():
            print("stackOverlow")
            return
        else:
            self.top += 1
            self.array.append(x)

    def pop(self):
        if self.isEmpty():
            print("No element in the stack")
            return
        else:
            self.top -= 1
            return self.array.pop()

class SpecialStack(Stack):
    def __init__(self):
        super().__init__()
        self.MinS = Stack()
    
    def push(self, x):
        if self.isEmpty():
            super().push(x)
            self.MinS.push(x)
        else:
            super().push(x)
            y = self.MinS.pop()
            self.MinS.push(y)
            if x < y:
                self.MinS.push(x)
            else:
                self.MinS.push(y)
    
    def pop(self):
        x = super().pop()
        self.MinS.pop()
        return x
    
    def getMin(self):
        x = self.MinS.pop()
        self.MinS.push(x)
        return x
    
if __name__ == "__main__":

    st = SpecialStack()
    st.push(10)
    st.push(12)
    st.push(5)
    st.push(6)
    st.push(7)
    st.push(1)

    print(st.getMin())

    st.pop()
    print(st.getMin())


    