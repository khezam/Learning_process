class HashTable:
    def __init__(self, length):
        self.table = [None] * length
        self.n = 0
    
    def first_hash(self, key):
        m = len(self.table)
        return key % m
    
    def second_hash(self, home, i):
        m = len(self.table)
        slot = (home + i) % m
        return slot
        
    def search(self, key):
        i = 0
        #Look for an empty slot from where key was intially maped
        home = self.first_hash(key)
        position = home
        while self.table[position] != None:
            if self.table[position] == key:
                return position
            i += 1
            position = self.second_hash(home, i)
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
            


# t = HashTable(13)
# t.insert(431)
# t.insert(96)
# t.insert(579)
# t.insert(765)
# t.insert(142)
# t.insert(226)
# t.insert(903)
# t.insert(388)
# t.delete(226)
# t.searchKey(903)
