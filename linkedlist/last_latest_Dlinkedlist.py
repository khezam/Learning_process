class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None
        
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        return self
        
    def preappend(self, element):
        if not self.head:
            self.append(element)
        else:
            new_node = Node(element)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
        return self
        
    def delete_first(self, element):
        if self.head:
            if self.head.element == element:
                self.head = self.head.next
                self.head.prev = None
                self.size -= 1
            else:
                return "Not Found"
        else:
            raise ValueError("List is empty")
        return self
        
    def delete_last(self, element):
        if self.head:
            if self.tail.element == element:
                self.tail = self.tail.prev
                self.tail.next = None
                self.size -= 1
                return self
            else:
                return "Not Found"
        else:
            raise ValueError("List is empty")
            
    def delete(self, element):
        if self.head:
            if self.head.element == element:
                self.delete_first(element)
                return self
            else:
                i = 1
                n = self.size 
                curr = self.head.next 
                while i < n:
                    if curr.element == element and curr != self.tail:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                        self.size -= 1
                        return self
                    elif curr.element == element and curr == self.tail:
                        self.delete_last(element)
                        return self
                    else:
                        i += 1
                        curr = curr.next
                return "Not found"
        else:
            raise ValueError("List is empty")

d = DLinkedList()

