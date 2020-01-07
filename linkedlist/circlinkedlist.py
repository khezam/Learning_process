class Node:
    
    def __init__(self, element, next = None):
        self.element = element
        self.next = next

class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, element):
        new_node = Node(element)
        
        if self.head != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.head = new_node
            new_node.next = self.head
            self.tail = new_node

    def reverse(self):
        curr = self.head.next
        prevCurr = self.head
        
        if self.tail.next == self.head:
            if prevCurr == self.head:
                self.head.next = None
        
        while curr != self.tail:
            prevCurr = curr
            curr = curr.next
            prevCurr.next = self.tail.next
            self.tail.next = prevCurr
        self.head.next = curr
        self.tail = self.head
        self.head = curr
            
    
l = CircularLinkedList()
# l.push(20)
# l.push(30)
# l.push(40)
# l.push(50)
# l.push(60)