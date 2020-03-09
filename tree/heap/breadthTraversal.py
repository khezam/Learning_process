# Implementation of the Queue ADT using a Python list
class Queue:
    """Circulry Queue"""
    def __init__(self):
        self.qList = list()
        
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.qList)
        
    def enqueue(self, element):
        return self.qList.append(element)
        
    def dequeue(self):
        return self.qList.pop(0)

class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def addNode(self, node, new_node):
        if node.element < new_node.element:
            if not node.right:
                node.right = new_node
                return node
            else:
                return self.addNode(node.right, new_node)
        else:
            if not node.left:
                node.left = new_node
                return node
            else:
                return self.addNode(node.left, new_node)
                
    def add(self, element):
        new_node = Node(element)
        if not self.root:
            self.root = new_node
            return self.root
        else:
            return self.addNode(self.root, new_node)
              
    def  breadth_traversal(self):
        q = Queue()
        q.enqueue(self.root)
        
        while not q.isEmpty():
            node = q.dequeue()
            print(node.element)
            
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
                
        return self.root
        
            
# b = BinaryTree()
# b.add(40)
# b.add(20)
# b.add(15)
# b.add(30)
# b.add(60)
# b.add(50)
# b.add(65)
# b.breadth_traversal()

"""
# Implementation of the Queue ADT using a Python list
class Queue:
    """Circulry Queue"""
    def __init__(self):
        self.qList = []
        
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.qList)
        
    def enqueue(self, element):
        return self.qList.append(element)
        
    def dequeue(self):
        return self.qList.pop(0)

class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def addNode(self, node, new_node):
        if node.element < new_node.element:
            if not node.right:
                node.right = new_node
                return node
            else:
                return self.addNode(node.right, new_node)
        else:
            if not node.left:
                node.left = new_node
                return node
            else:
                return self.addNode(node.left, new_node)
                
    def add(self, element):
        new_node = Node(element)
        if not self.root:
            self.root = new_node
            return self.root
        else:
            return self.addNode(self.root, new_node)
              
    def  breadth_traversal(self):
        q = Queue()
        q.enqueue(self.root)
        
        lst = []
        while not q.isEmpty():
            node = q.dequeue()
            if node == None:
                lst.append(node)
               
            if node:
                if node.left or not node.left:
                    q.enqueue(node.left)
                if node.right or not node.right:
                    q.enqueue(node.right)
                lst.append(node.element)
                
        return lst
        
            
b = BinaryTree()

"""
