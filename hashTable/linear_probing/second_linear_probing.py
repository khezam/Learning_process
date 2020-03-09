class HashTable:
    def __init__(self, length):
        self.table = [None] * length
        self.n = 0
    
    def hash(self, key, i):
        m = len(self.table)
        slot = ((key % m) + i) % m
        return slot
        
    def search(self, key):
        i = 0
        position = self.hash(key, i)
        while self.table[position] != None:
            if self.table[position] == key:
                return position
            i += 1
            position = self.hash(position, i)
        if not self.table[position]:
            return position
        
        return "Slots are full"
        
    def insert(self, key):
        slot = self.search(key)
        if self.table[slot] != None:
            return slot
        self.table[slot] = key
        self.n += 1
        return self.table
        
    def delete(self, key):
        slot = self.search(key)
        if self.table[slot] == key:
            self.table[slot] = -1
            return self.table 
        return "Not found"
        
    def searchKey(self, key):
        slot = self.search(key)
        if self.table[slot] != key:
            return "Not found"
        return "found"
            


t = HashTable(13)
# t.insert(431)
# t.insert(96)
# t.insert(579)
# t.insert(765)
# t.insert(142)


