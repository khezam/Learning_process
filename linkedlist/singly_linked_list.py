class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.list = None
    # Append a node to the end
    def append(self, data):
        new_node = Node(data)
        
        if self.list != None:
            curr = self.list
            while curr.next_node != None:
                curr = curr.next_node
            curr.next_node = new_node
        else:
            self.list = new_node

    # Insert a node at any position of the list. If the index is greater than the zise of the list, then insert it at the end      
    def insert(self, data, index):
        if index == 0:
            new_node = Node(data)
            curr = self.list
            new_node.next_node = curr
            self.list = new_node
        else:
            new_node = Node(data)
            curr = self.list
            while index > 1:
                if curr.next_node == None:
                    break
                curr = curr.next_node
                index -=1
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    # Preappend a node to the beginning of the list        
    def preappend(self, data):
        new_node = Node(data)
        new_node.next_node = self.list
        self.list = new_node
    
    def search(self, key):
        curr = self.list
        while curr.next_node != None:
            if curr.data == key:
                return key
            else:
                curr = curr.next_node
        if curr.data == key:
            return key
        return False
    
    # Remove a node by by passing the value of that node  
    def remove(self, value):
        curr = self.list.next_node
        prevPointer = self.list
        found = False

        if prevPointer.data == value:
            prevPointer.next_node = None
            self.list = curr
            return
        
        while curr.next_node != None and found:
            if curr.data == value:
                found = True
                currPointer = curr.next_node
                prevPointer.next_node = None
                curr.next_node = None
                prevPointer.next_node = currPointer
            else:
                curr = curr.next_node
                prevPointer = prevPointer.next_node
         
        if (curr.next_node == None and curr.data == value) and found == False:
                prevPointer.next_node = None
            
     
l = LinkedList()

# l.append(0)
# l.append(888)
# l.append(777)
# l.append(111)
# l.append(555)
# l.insert(10, 0)
# l.insert(555, 3)
# l.insert(33, 10)
# l.append(666)
# l.preappend(2222)
# l.preappend(1111)
# l.search(999)
# l.remove(777)
