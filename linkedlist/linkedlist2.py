class Node:
    
    def __init__(self, element, next = None):
        self.element = element
        self.next = next 
  
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.element)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.element)
            else:
                nodes.append("[%s]" % current.element)
            current = current.next
        return  '-> '.join(nodes)
    
    def is_empty(self):
        return self.size == 0
    
    """Add element element to the top of the stack"""
    def push(self, element):
        new_node = Node(element)
        
        if self.head != None:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            self.size += 1
        else:
            self.head  = new_node
            self.size += 1
    
    """Return the first top element in the stack"""
    def top(self):
        if self.is_empty():
            raise("Stack is empty")
        
        curr = self.head 
        while curr.next != None:
            curr = curr.next
        return curr
    
    """Removes and return the first top element in the stack"""
    def pop(self):
        if self.is_empty():
            raise("Stack is empty")
        
        curr = self.head.next 
        prevCurr = self.head 
        
        while curr.next != None:
            curr = curr.next
            prevCurr = prevCurr.next
        prevCurr.next  = None
        return curr
    
    """Return the index of the key"""
    def search(self, key):
        if not self.is_empty():
            curr = self.head
            
            counter  = self.size 
            while curr.next != None:
                if curr.element == key:
                    return (self.size - counter) + 1
                curr = curr.next
                counter -= 1
            if curr.element == key:
                return (self.size - counter) + 1
            return False
        return "Stack is empty"
    
    """Insert a node at any arbitrary index within the linked-list""" 
    def insert(self, index, element): 
        if not self.is_empty():
            if index > self.size:
                self.push(element)
            elif index == 0:
                new_node = Node(element)
                new_node.next = self.head
                self.head = new_node
                self.size +=1
            else:
                new_node = Node(element)
                curr = self.head.next
                prevCurr = self.head
                index = index - 1
                while index > 1:
                    if curr.next != None:
                        curr = curr.next
                        prevCurr =  prevCurr.next
                        index -= 1
                    else:
                        break
                new_node.next = prevCurr.next
                prevCurr.next = new_node
                self.size += 1
        return "Stack is empty"
            
    """Remove a node based on the given element"""     
    def remove(self, value):
        if not self.is_empty():
            curr = self.head.next
            prevCurr = self.head
            found = False
            
            if prevCurr.element == value:
                self.head = curr
                prevCurr.next = None
                return
            else:
                while curr.next != None and found != True:
                    if curr.element == value:
                        found = True
                        prevCurr.next = curr.next
                        curr.next = None
                    else:
                        curr = curr.next
                        prevCurr = prevCurr.next
                if (curr.next == None and curr.element == value) and found == False:
                    prevCurr.next = None
                return False
        return "Stack is empty"

    """Reverse the linked-list"""
    def reverse(self):
        curr = self.head.next
        prevCurr = self.head
        prev = None
        
        while curr.next != None:
            prevCurr.next = prev
            prev = prevCurr
            prevCurr = curr
            curr = curr.next
            prevCurr.next = prev
        curr.next = prevCurr
        self.head = curr

    # def reverse(self):
    #     curr = self.head.next
    #     prevCurr = self.head
    
    #     while curr.next != None:
    #         cpPrevCurr = prevCurr
    #         prevCurr = curr
    #         curr = curr.next
    #         prevCurr.next = cpPrevCurr
    #     curr.next = prevCurr
    #     self.head.next = None
    #     self.head = curr

    # def reverse(self):
    #     curr = self.head
    #     prevCurr = None
        
    #     while curr != None:
    #         next = curr.next
    #         curr.next = prevCurr
    #         prevCurr = curr
    #         curr = next
    #     self.head = prevCurr

    # def reverse(self):
    #     curr = self.head.next
    #     prevCurr = self.head
        
    #     if self.head != None:
    #         self.head.next = None
        
    #     while curr.next != None:
    #         prevCurr = curr
    #         curr = curr.next
    #         prevCurr.next = self.head
    #         self.head = prevCurr
    #     curr.next = prevCurr
    #     self.head = curr
    
l = LinkedList()
# l.push(3)
# l.push(4)
# l.push(1)
# l.push(9)
# l.push(8)
# l.push(6)
# l.push(7)
# l.insert(1, 8888888)
