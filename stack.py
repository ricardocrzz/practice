#LIFO Last In First Out

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
#peek without deleting
print(stack.peek())
print(stack.size())

#or using prebuilt, deque
from collections import deque

# Creating a stack
stack = deque()
# Usage
stack.append(1)
stack.append(2)
print(stack.pop())  # Output: 2

topElement = stack[-1] if stack else None
print(topElement)
isEmpty = len(stack) == 0
print(isEmpty)

#just using a list
# Creating a stack
stack = []

# Adding elements to the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Removing elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
