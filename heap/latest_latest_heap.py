class MaxHeap:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size 
        self.count = -1 
        
    def insert(self, element):
        if not self.count + 1:
            self.array[self.count+1] = element
            self.count += 1
            return self.array
        self.array[self.count+1] = element
        self.count += 1
        return self.siftUp(self.count)
        
    def swap(self, left, right):
        tmp = self.array[right]
        self.array[right] = self.array[left]
        self.array[left] = tmp
        return self.array
    
    def siftUp(self, position):
        parent = (position - 1) // 2
        if position <= 0 or self.array[position] <= self.array[parent]:
            return self.array
        self.swap(parent, position)
        return self.siftUp(parent)
        
    def extract(self):
        if not self.count:
            return "Heap is empty"
        tmp = self.array[0]
        self.array[0] = self.array[self.count]
        self.array[self.count] = None
        self.count -= 1
        self.siftDown(0)
        return tmp
        
    def siftDown(self, position):
        left = (2 * position) + 1
        right = (2 * position) + 2
        if left >= self.count or right >= self.count:
            if left == self.count and self.array[position] < self.array[left]:
                return self.swap(position, left)
            if right == self.count and self.array[position] < self.array[right]:
                return self.swap(position, right)
            return self.array
        elif self.array[left] > self.array[right] and self.array[left] > self.array[position]:
            self.swap(position, left)
            return self.siftDown(left)
        elif self.array[right] > self.array[left] and self.array[right] > self.array[position]:
            self.swap(position, right)
            return self.siftDown(right)
        return self.array
        
    def sort(self):
        n = self.count
        i = 0
        while i < n:
            tmp = self.extract()
            self.array[n] = tmp
            n -= 1
        return self.array
        

# h = MaxHeap(7)
# h.insert(90)
# h.insert(60)
# h.insert(20)
# h.insert(30)
# h.insert(27)
# h.insert(10)
# h.insert(15)
# h.sort()



        