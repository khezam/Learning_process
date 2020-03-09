class MaxHeap:
    def __init__(self, size):
        self.array = [None] * size 
        self.count = 0
        
    def insert(self, element):
        if not self.count:
            self.array[self.count] = element
            self.count += 1
            return self.array
        self.array[self.count] = element
        self.count += 1
        return self.siftUp(self.count-1)
        
    def swap(self, left, i):
        tmp = self.array[left]
        self.array[left] = self.array[i]
        self.array[i] = tmp
        return self.array
    
    
    def siftUp(self, last):
        parent = (last-1) // 2
        if last <= 0 or  self.array[last] <= self.array[parent]:
            return self.array
        self.swap(last, parent)
        return self.siftUp(parent)
    
    def remove(self):
        i = 0
        n = len(self.array) - 1
        self.array[i] = self.array[n]
        self.array[n] = None
        n -= 1
        return self.siftDown(i, n)
        
    def siftDown(self, i, n):
        left = (2 * i) + 1
        right = (2 * i) + 2
        if left >= n or right >= n:
            if left == n and self.array[i] < self.array[left]:
                self.swap(left, i)
                return self.array
            if right == n and self.array[i] < self.array[right]:
                self.swap(left, i)
                return self.array
        elif self.array[left] > self.array[right] and self.array[left] > self.array[i]:
            self.swap(left, i)
            return self.siftDown(left, n)
        elif self.array[right] > self.array[left] and self.array[right] > self.array[i]:
            self.swap(left, i)
            return self.siftDown(right, n)
                

# heap = MaxHeap(5)
# heap.insert(20)
# heap.insert(10)
# heap.insert(15)
# heap.insert(30)
# heap.insert(40)
# heap.remove()