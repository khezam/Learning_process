class Node:
    
    def __init__(self, e, prev = None, next = None):
        self.e = e
        self.prev = prev
        self.next = next
        
class DoublyLinkedBase:
    
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0
    
    """Its the same as the push function but less cleaner"""    
    # def push(self, e):
    #     new_node = Node(e)
        
    #     if self.head == None:
    #         self.head = new_node
    #         self.tail = new_node 
        
    #     elif self.tail.next == None:
    #         self.tail.next = new_node
    #         new_node.prev = self.tail
    #         self.tail = new_node
    
    def push(self, e):
        new_node = Node(e)
        """If self.head is truly not None"""
        if self.head:
            """If self.tail.next is truly None"""
            if not self.tail.next:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                self.size += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.size +=1

    """Insert at the first position"""
    def insert(self, e):
        new_node = Node(e)
        """If self.head is not None"""
        if self.head:
            """If self.head.prev is truly None"""
            if not self.head.prev:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.size += 1
        else:
            self.push(e)
            self.size += 1
            
    """Insert Node at any"""
    def insert_node(self, e, key):
        new_node = Node(e)
        curr = self.head
        counter = 0
        key = key - 1
        
        if self.head:
            while counter != key:
                curr = curr.next
                counter += 1
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev = new_node
            self.size += 1
                
            
            

        
            
        
l = DoublyLinkedBase()
l.push(22)
l.push(33)
l.push(44)
l.push(55)
l.push(66)
l.push(77)