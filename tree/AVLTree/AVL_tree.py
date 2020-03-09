class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.parent = None

class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def addNode(self, parent, element):
        new_node = Node(element)
        if parent.element < element:
            if not parent.right:
                parent.right = new_node
                new_node.parent = parent
                self.size +=1 
            else:
                self.addNode(parent.right, element)
        else:
            if not parent.left:
                parent.left = new_node
                new_node.parent = parent
                self.size += 1
            else:
                self.addNode(parent.left, element)
                
        self.checkBalance(new_node)
        
    def maxHeight(self, node):
        if not node:
            return -1
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            return max(left, right) + 1
        
    def checkBalane(self, node):
        if (self.maxHeight(node.left) - self.maxHeight(node.right)) > 1 or (self.maxHeight(node.left) - self.maxHeight(node.right)) < -1:
            self.rebalance(node)
            
        if not node.parent:
            return 
        else:
            self.checkBalance(node.parent)
            
    def rebalance(self, node):
        if (self.maxHeight(node.left) - self.maxHeight(node.right)) > 1:
            if self.maxHeight(node.left.left) > self.maxHeight(node.left.right):
                node = self.rightRotate(node)
            else:
                node = self.leftRightRotate(node)
        else:
            if self.maxHeight(node.right.left) > self.maxHeight(node.right.right):
                node = self.leftRotate(node)
            else:
                node = self.rightleftRotate(node)
        if not node.parent:
            self.root = node
        
    def leftRotate(self, node):
        tmp = node.right 
        node.right = tmp.left
        tmp.left = node
        self.root = tmp
        return tmp        
    
    def rightRotate(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        self.root = tmp
        return tmp
        
    def leftRightRotate(self, node):
        node.left = self.leftRotate(node.left)
        return self.rightRotate(node)
        
    def rightLeftRotate(self, node):
        node.right = self.rightRotate(node.right)
        return self.leftRotate(node)

    def add(self, element):
        if not self.root:
            self.root = Node(element)
            self.size += 1
            return self.root
        else:
            return self.adNode(self.root, element)

