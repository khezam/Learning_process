class Qeue:
    """Circulry Queue"""
    def __init__(self, maxSize):
        self.array = [None] * maxSize
        self.count = 0
        self.front = 0
        self.back = len(self.array) - 1
        
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == len(self.array)
    
    def __len__(self):
        return self.count
        
    def enqueue(self, element):
        if self.isFull():
            return "Queue is full"
        else:
            if self.back == len(self.array) - 1:
                self.back = 0
            else:
                self.back += 1
            self.array[self.back] = element
            self.count += 1
        return self.array
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            element = self.array[self.front]
            self.array[self.front] = None
            if self.front == len(self.array) - 1:
                self.front = 0
            else:
                self.front += 1
                self.count -= 1
        return element

# q = Qeue(8)
# q.enqueue(1)    
# q.enqueue(2)          
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)
# q.enqueue(8)
        
