class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def preappend(self, element):
        if not self.head:
            self.append(element)
        else:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        return self
        
        
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1
        return self.head
        
    def pop(self):
        if self.head:
            node = self.head
            while node.next.next:
                node = node.next
            self.tail = node
            node.next = None
            self.count -= 1
            return self.head
        return "Stack is empty"
        
    def dequeue(self):
        if self.head:
            self.head = self.head.next
            self.count -= 1
            return self.head
        return "Queue is empty"
        
    def _search(self, element):
        if self.head:
            node = self.head
            while node and node.element != element:
                prev = node
                node = node.next
            if not node:
                return 
            return prev
        return
    
    def search(self, element):
        prev = self._search(element)
        if prev:
            return True
        return 
        
    def delete(self, element):
        if self.head:
            prev = self._search(element)
            if prev:
                if prev.next.next:
                    prev.next = prev.next.next
                    self.count -= 1
                    return self.head
                self.tail = prev
                prev.next = None
                self.count -= 1
                return self.head
            return "Not found"
        return "No nodes avail"

    def insert(self, index, element):
        if self.head:
            index = index - 1
            if index <= 1:
                return self.preappend(element)
            elif index > 1 and index < self.count:
                new_node = Node(element)
                node = self.head
                i = 1
                while i < index:
                    i += 1
                    node = node.next 
                new_node.next = node.next
                node.next = new_node
                self.count += 1
                return self.head
            else:
                return self.append(element)
        return "No nodes avai"
        
    def reverse(self, node):
        if not node or not node.next:
            return node
        curr = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return curr

    def reverse(self, node):
        if not node or not node.next:
            return node
        curr = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return curr

    
        
    def cyrclePos(self, index):
        i = 0
        node = self.head
        while i < self.count and i != index:
            i += 1
            node = node.next
        self.tail.next = node
        self.tail = None
        return self.head
        
    def cyrcle(self):
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
def intersection(headA, headB):
    nodeA = headA
    nodeB = headB
    if not nodeA or not nodeA.next:
        return False
    if not nodeB or not nodeB.next:
        return False
        
    while nodeA != nodeB:
        if nodeA != nodeB and nodeA.next == None and nodeB.next == None:
            return False
        if nodeA.next == nodeB.next:
            return nodeA.next
        if not nodeA.next:
            nodeA = headA
        if not nodeB.next:
            nodeB = headB
        nodeA = nodeA.next
        nodeB = nodeB.next
    return nodeA

    # def cyrcle(self):
    #     i = self.head
    #     if not i:
    #         return
    #     if not i.next:
    #         return i
    #     while i and i.next:
    #         if i.next == self.head:
    #             return i.next
    #         j = self.head
    #         while j.next != i.next and j != i and j != i.next:
    #             j = j.next
    #         if j == i:
    #             i = i.next
    #             j = self.head
    #         elif j.next == i.next or j == i.next:
    #             return i.next
    #     return "It's not cyricular"


            
l = LinkedList()
l.append(3)
l.append(2)
l.append(0)
l.append(-4)
l.append(19)
l.append(6)
l.append(-9)

print(l.count)
l.cyrclePos(l.coun)
print(l.cyrcle().element)
