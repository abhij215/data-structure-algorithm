from sys import maxsize

# function to create a stack
def createStack():
    stack = []
    return stack

# returns true if its empty else false
def isEmpty(stack):
    return len(stack) == 0


# appends new elements to the stack
def push(stack,item):
    stack.append(item)

# removes the last element
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
    return stack.pop()

#return the last element
def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
    return stack[-1]


# main function
st1 = createStack()
push(st1, 12)
push(st1, 13)
push(st1, 14)
push(st1, 16)
push(st1, 20)

last = peek(st1)

print(st1)
print(last)
