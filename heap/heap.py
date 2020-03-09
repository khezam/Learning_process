class MaxHeap:
    def __init__(self):
        self.array = [100, 84, 71, 60, 23, 12, 29, 1, 37, 4, None]
        self.count = len(self.array) - 2
        
    def insert(self, element):
        self.array[self.count+1] = element
        self.count += 1
        
        return self.siftUp()
        
    def siftUp(self):
        first = 0
        last = self.count
        while first <= last:
            parent = (last -1) // 2
            if self.array[parent] < self.array[last]:
                tmp = self.array[last]
                self.array[last] = self.array[parent]
                self.array[parent] = tmp
                last = parent
            else:
                return self.array

    def swap(self, parent, child):
        tmp = self.array[child]
        self.array[child] = self.array[parent]
        self.array[parent] = tmp
    # Remove the root's element         
    def extract(self):
        first = 0
        last = self.count - 1
        self.array[first] = self.array[last + 1]
        self.array[last + 1] = None
        self.count -= 1
        return self.siftDown(first, last)
    
    def siftDown(self, first, last):
        while first < last:
            left = (2 * first) + 1
            right = (2 * first) + 2
            if self.array[left] and self.array[right]:
                if self.array[left] > self.array[right]:
                    self.swap(first, left)
                    first = left
                else:
                    self.swap(first, right)
                    first = right
            else:
                if self.array[left] and self.array[first] < self.array[left]:
                    self.swap(first, left)
                    return 
                elif self.array[right] and self.array[first] < self.array[right]:
                    self.swap(first, right)
                    return 
                


heap = MaxHeap()
heap.insert(90)