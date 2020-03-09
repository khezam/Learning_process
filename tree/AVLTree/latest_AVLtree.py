class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.parent = None
        
class AVLTree:
    def __init__(self):
        self.root = None
        
        
    def addNode(self, node, new_node):
        if node.element < new_node.element:
            if not node.right:
                node.right = new_node
                new_node.parent = node
            else:
                return self.addNode(node.right, new_node)
        else:
            if not node.left:
                node.left = new_node
                new_node.parent = node
            else:
                return self.addNode(node.left, new_node)
        return self.is_balance(new_node)
                
    def add(self, element):
        new_node = Node(element)
        if not self.root:
            self.root = new_node
            return self.root
        else:
            return self.addNode(self.root, new_node)
            
    def is_balance(self, node):
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        print(leftHeight - rightHeight)
        
        if leftHeight - rightHeight > 1:
            return self.rebalanceRight(node)
            
        elif leftHeight - rightHeight < -1:
            return self.rebalanceLeft(node)
            
        elif not node.parent:
            return 
        
        return self.is_balance(node.parent)
        
    def rebalanceRight(self, node):
        leftHeight = self.height(node.left.left)
        rightHeight = self.height(node.left.right)
        if leftHeight > rightHeight: 
            node = self.rightRotate(node)
            return node
        else:
            node = self.leftRightRotate(node)
            return node
    
    def rebalanceLeft(self, node):
        leftHeight = self.height(node.right.right)
        rightHeight = self.height(node.right.left)
        if leftHeight > rightHeight: 
            node = self.leftRotate(node)
            return node
        else:
            node = self.rightLeftRotate(node)
            return node
            
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
        
    def height(self, node):
        if not node:
            return -1
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            return max(left, right) + 1

b = AVLTree()
