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
        print(abs(leftHeight - rightHeight))
        if leftHeight - rightHeight > 1:
          return self.rebalanceRight(node)
        elif leftHeight - rightHeight < -1:
          return self.rebalanceLeft(node)
        elif not node.parent:
            return 
        return self.is_balance(node.parent)
            
    
    def rebalanceLeft(self, node):
        leftHeight = self.height(node.right.right)
        rightHeight = self.height(node.right.left)
        if leftHeight > rightHeight: 
            node = self.leftRotate(node)
            return node
        else:
            node = self.rightLeftRotate(node)
            return node
    
    def rebalanceRight(self, node):
        leftHeight = self.height(node.left.left)
        rightHeight = self.height(node.left.right)
        if leftHeight > rightHeight: 
            node = self.rightRotate(node)
            return node
        else:
            node = self.leftRightRotate(node)
            return node
            
    def leftRotate(self, node):
        tmp = node.right
        if tmp.left:
            tmp.left.parent = node
        node.right = tmp.left
        tmp.left = node
        if node == self.root:
            node.parent = tmp
            tmp.parent = None
            self.root = tmp
            return tmp
        else:
            tmp.parent = node.parent
            node.parent = tmp
            tmp.parent.left = tmp
            return self.root
            
    def leftRightRotate(self, node):
        tmp = node.left.right
        tmp.parent  = node
        node.left.right = tmp.left
        node.left.parent = tmp
        tmp.left = node.left
        node.left = tmp
        return self.rightRotate(node)
            
    def rightRotate(self, node):
        tmp = node.left
        if tmp.right:
            tmp.right.parent = node
        node.left = tmp.right
        tmp.right = node
        if not node.parent:
            node.parent = tmp
            tmp.parent = None
            self.root = tmp
            return tmp
        else:
            tmp.parent = node.parent
            node.parent = tmp
            tmp.parent.left = tmp
            return self.root
    
    def rightLeftRotate(self, node):
        tmp = node.right.left
        tmp.parent  = node
        node.right.left = tmp.right
        node.right.parent = tmp
        tmp.right = node.right
        node.right = tmp
        return self.leftRotate(node)
    
    def height(self, node):
        if not node:
            return -1
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            return max(left, right) + 1
        
            
    
b = AVLTree()
# b.add(43)
# b.add(18)
# b.add(22)
# b.add(9)
# b.add(21)
# b.add(6)
# b.add(8)
# b.add(20)

