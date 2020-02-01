class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # def __repr__(self):
    #     """
    #     Return a string representation of the list.
    #     Takes O(n) time.
    #     """
    #     nodes = []
    #     current = self.head
    #     while current:
    #         if current is self.head:
    #             nodes.append("[%s]" % current.element)
    #         elif current.next is None:
    #             nodes.append("[%s]" % current.element)
    #         else:
    #             nodes.append("[%s]" % current.element)
    #         current = current.next
    #     return  '-> '.join(nodes)

    def diplayLinkedList(self, curr):
        """Linkedlist that represented in string format"""
        string = ""
        """Base case: if curr.next == None"""
        if curr.next:
            nodes = self.diplayLinkedList(curr.next)
            string += nodes
        """At the current node, preappend the element into the string"""
        string =  f"{curr.element}-> " + string
        return string
    
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        return self
    
    def preappend(self, element):
        if not self.head:
            self.append(element)
        else:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        return self
        
    def insert(self, element, index):
        if self.head:
            index = index - 1
            if index < 1:
                self.preappend(element)
            elif index >= 1 and index < self.size:
                new_node = Node(element)
                curr = self.head
                i = 1
                while i < index:
                    curr = curr.next
                    i += 1
                new_node.next = curr.next
                curr.next = new_node
                self.size += 1
            else:
               self.append(element) 
        else:
            self.append(element)
        return self
        
    def remove(self, index):
        if self.head:
            if index > self.size:
                raise IndexError("Out of index")
            elif index > 1 and index <= self.size:
                i = 1
                index = index - 1
                curr = self.head
                while i < index:
                    curr = curr.next
                    i += 1
                if curr.next.next != None:
                    curr.next = curr.next.next
                else:
                    self.tail = curr
                    curr.next = None
            else:
                self.head = self.head.next
            self.size -= 1
            return self
        else:
            raise IndexError("Stack is empty")


    # This functio below is the old version that I created       
    # def delete(self, target):
    #     if self.head:
    #         if self.head.element == target:
    #             self.head = self.head.next
    #             self.size -= 1
    #             return self
    #         else:
    #             curr = self.head
    #             i = 0
    #             n = self.size - 1
    #             while i < n:
    #                 if curr.next.element == target and curr.next.next != None:
    #                     curr.next = curr.next.next
    #                     self.size -= 1
    #                     return self
    #                 elif curr.next.element == target and curr.next.next == None:
    #                     curr.next = None
    #                     self.tail = curr
    #                     self.size -= 1
    #                     return self
    #                 else:
    #                     curr = curr.next
    #                     i += 1
    #             return "Not found"
                          
    #     else:
    #         raise ValueError("No values in the list")

    def delByElement(self, element):
        if self.head:
            if self.head.element == element:
                self.head = self.head.next
                self.size -= 1
                return self

            curr = self.head
            while curr.next:
                if curr.next.element == element:
                    """If curr.next.next is not None""" 
                    if curr.next.next:
                        curr.next = curr.next.next
                    else:
                        """If curr.next.next is None: that means curr is one less the last node"""
                        self.tail = curr
                        curr.next = None
                    self.size -= 1
                    return self

                curr = curr.next
            return "Not Found"
        else:
            raise IndexValue("List is empty")

    """Circular LinkedList Function"""
    def circNode(self, element):
        if self.head:
            self.append(element).tail.next = self.head
        else:
            self.append(element)
            self.tail.next = self.head
        return self
            
l = Linkedlist()
# l.append(5)
# l.append(4)
# l.append(3)
# l.append(2)
# l.append(1)
# print(l)
