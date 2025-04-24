# 44. Implement a queue using deque.
from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
    def enqueue(self,i):
        self.queue.append(i)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
    def is_empty(self):
        
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


q1=Queue()
print(q1.dequeue())
q1.enqueue(12)
q1.enqueue(122)
q1.enqueue(1232)
q1.enqueue(1212)

print(q1.peek())

print("Dequeued:", q1.dequeue())  # Output: Dequeued: 10
print("Next item:", q1.peek())    # Output: Next item: 20
print("Queue size:", q1.size())   # Output: Queue size: 2