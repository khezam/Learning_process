# The list-based implementation of the Queue ADT
class Queue:
    def __init__(self):
        self.array = [None] * 10
        self.count = 0
    
    def is_Empty(self):
        return len(self) == 0
        
    def is_Full(self):
        return self.count == len(self.array)
    
    def enqueue(self, element):
        if self.count >= len(self.array):
            return "Queue is full"
        self.array[self.count] = element
        self.count += 1
        return self.array
    
    def dequeue(self):
        i = 0
        element = self.array[i]
        self.array[i] = None
        n = self.count-1
        while i < n:
            self.array[i] = self.array[i+1]
            i += 1
        self.array[i] = None
        return element
        
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)
# q.enqueue(8)
# q.enqueue(9)
# q.enqueue(10)
# q.enqueue(11)
