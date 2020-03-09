class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.m = len(self.table)
        self.n = 0
        
    # Original hash function
    def hash(self, key):
        return key % self.m
    
    # Calling the double hansh function
    def second_hash(self, home, i, key):
        slot = (home + i*self.double_hash(key)) % self.m
        return slot
        
    def double_hash(self, key):
        P = 8
        return 1 + key % P
        
    def search(self, key):
        i = 0
        home = self.hash(key)
        slot = home
        while self.table[slot] != None:
            if self.table[slot] == key:
                return slot
            i += 1
            slot = self.second_hash(home, i, key)
        if not self.table[slot]:
            return slot
        return "Table is full"
        
    def insert(self, key):
        slot = self.search(key)
        if self.table[slot] != None:
            return slot
        self.table[slot] = key
        self.n += 1
        return self.table
        
    def delete(self, key):
        slot = self.search[key]
        if slot == key:
            self.table[slot] = -1
            return self.table
        return "Not found"
        
    def searchKey(self, key):
        slot = self.search(key)
        if self.table[slot] != key:
            return "Not found"
        return "found"
            
        
# t = HashTable(13)
# t.insert(765)
# t.insert(431)
# t.insert(96)
# t.insert(142)
# t.insert(579)
# t.insert(226)
# t.insert(903)
# t.insert(388)
            