class MaxHeap:
    def __init__(self):
        self.array = [40, 30, 20, 25, 27, 10, 15, 60, None]
        self.count = len(self.array) - 2
        
    
    def insert(self, element):
        self.array[self.count + 1] = element
        self.count += 1
        last = len(self.array) - 1
        return self.siftUp(last)
    
    def siftUp(self, last):
        parent = (last-1) // 2
        if last <= 0 or  self.array[last] <= self.array[parent]:
            return self.array
        tmp = self.array[last]
        self.array[last] = self.array[parent]
        self.array[parent] = tmp
        return self.siftUp(parent)
        
    def remove(self):
        i = 0
        n = len(self.array) - 1
        self.array[i] = self.array[n]
        self.array[n] = None
        n -= 1
        return self.siftDown(i, n)
    
    def swap(self, left, i):
        tmp = self.array[left]
        self.array[left] = self.array[i]
        self.array[i] = tmp
        return self.array
        
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
            return self.array
        elif self.array[left] > self.array[right] and self.array[left] > self.array[i]:
            self.swap(left, i)
            return self.siftDown(left, n)
        elif self.array[right] > self.array[left] and self.array[right] > self.array[i]:
            self.swap(left, i)
            return self.siftDown(right, n)
        
        
h = MaxHeap()
h.insert(90)
h.remove()
        