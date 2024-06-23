from collections import deque

class Queue:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.l_queue = deque()
    
    def is_empty(self):
        return len(self.l_queue) == 0
    
    def is_full(self):
        return len(self.l_queue) == self.capacity
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self.l_queue.popleft()
    
    def enqueue(self, value):
        if value is None:
            raise ValueError("Cannot enqueue None value")
        if self.is_full():
            raise IndexError("Cannot enqueue into full queue")
        self.l_queue.append(value)
    
    def front(self):
        if self.is_empty():
            raise IndexError("Cannot get front of empty queue")
        return self.l_queue[0]
    
# Example usage based on provided examples
queue1 = Queue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())  # False

print(queue1.front())  # 1

print(queue1.dequeue())  # 1

print(queue1.front())  # 2

print(queue1.dequeue())  # 2

print(queue1.is_empty())  # True
