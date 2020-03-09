class HashTable:
    def __init__(self):
        self.table = [None] * 11
    
    def hash(self, key):
        return key % len(self.table)
        
    def insert(self, key):
        position = self.hash(key)
        if not self.table[position]:
            self.table[position] = key
            return self.table
        i = position + 1
        n = len(self.table) - 1
        while position != i:
            if i == n or self.table[i] == None:
                if self.table[i] == None:
                    return "Not found"
                i = -1
            i += 1
        return "No slots available"
    
    def delete(self, key):
        position = self.hash(key)
        if not self.table[position]:
            return "There no in the slot"
        if key == self.table[position]:
            self.table[position] = -1
            return self.table
        return "No match"
        
    def search(self, key):
        position = self.hash(key)
        if self.table[position] == key:
            return "True"
        if self.table[position] == -1 or self.table[position] != key:
            i = position + 1
            n = len(self.table) - 1
            while position != i:
                if i == n or self.table[i] == None:
                    if self.table[i] == None:
                        return "There no value equal to the given key"
                    i = -1
                elif self.table[i] == key:
                    return "Found at slot {}".format(i)
                i += 1
            return "No matching key"
            
            

table = HashTable()
# table.insert(0)
# table.insert(1)
# table.insert(2)
# table.insert(3)
# table.insert(4)
# table.insert(5)
# table.insert(666)
# table.insert(7)
# table.insert(8)
# table.insert(9)
# table.insert(10)
# table.delete(7)
# table.delete(10)
# table.insert(6)
# table.search(6)
