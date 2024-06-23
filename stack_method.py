class Stack:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.l_stack = []
    
    def is_empty(self):
        return len(self.l_stack) == 0
    
    def is_full(self):
        return len(self.l_stack) == self.capacity
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self.l_stack.pop()
    
    def push(self, value):
        if self.is_full():
            raise IndexError("Cannot push into full stack")
        self.l_stack.append(value)
    
    def top(self):
        if self.is_empty():
            raise IndexError("Cannot get top of empty stack")
        return self.l_stack[-1]
# Example usage based on provided examples
stack1 = Stack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())  # False

print(stack1.top())  # 2

print(stack1.pop())  # 2

print(stack1.top())  # 1

print(stack1.pop())  # 1

print(stack1.is_empty())  # True