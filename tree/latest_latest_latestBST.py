class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BinarySearch:
    def __init__(self):
        self.root = None
    
    def add(self, element):
        if not self.root:
            self.root = Node(element)
            return self.root
        else:
            return self.addNode(self.root, element)
    
    def addNode(self, node, element):
        if node.element < element:
            if not node.right:
                node.right = Node(element)
                return node
            else:
                return self.addNode(node.right, element)
        else:
            if not node.left:
                node.left = Node(element)
                return node
            else:
                return self.addNode(node.left, element)
                
    def size(self, node):
        if not node:
            return 0
        else:
            left = self.size(node.left)
            right = self.size(node.right)
            return (left + right) + 1
            
    def maxHeight(self, node):
        if not node:
            return -1
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            return max(left, right) + 1
            
    def minHeight(self, node):
        if not node:
            return -1
        else:
            left = self.minHeight(node.left)
            right = self.minHeight(node.right)
            return min(left, right) + 1
            
    def maxDepth(self, node):
        if not node:
            return 0 
        else:
            left = self.maxDepth(node.left)
            right = self.maxDepth(node.right)
            return max(left, right) + 1
            
    def minDepth(self, node):
        if not node:
            return 0
        else:
            left = self.minDepth(node.left)
            right = self.minDepth(node.right)
            return min(left, right) + 1
            
    def maxValue(self, node):
        if not node.right:
            return node.element
        else:
            return self.maxValue(node.right)
    
    def minValue(self, node):
        if not node.left:
            return node.element
        else:
            return self.minValue(node.left)
            
    def search(self, node, target):
        if not node:
            return False
        elif node.element == target:
            return node.element
        elif node.element < target:
            return self.search(node.right, target)
        else:
            return self.search(node.left, target)
            
    def traverse(self, node):
        if not node.left.left:
            successor = node.left.element
            node.left = None
            return successor
        else:
            return self.traverse(node.left)
            
    def remove(self, node, target):
        if not node:
            return None
        elif node.element == target:
            if not node.left and not node.right:
                return None
            elif node.left and node.right:
                node.element = self.traverse(node.right)
                return node
            else:
                if node.left:
                    return node.left
                else:
                    return node.right
        elif node.element < target:
            node.right = self.remove(node.right, target)
            return node
        else:
            node.left = self.remove(node.left, target)
            return node

    # Left rotate when a BST is unbalanced that looks like a singly linkedlist
    def leftRotate(self, node):
        tmp = node.right 
        node.right = tmp.left
        tmp.left = node
        self.root = tmp
        return tmp
     
    # Right rotate when a BST is unbalanced that looks like a singly linkedlist
    def rightRotate(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        self.root = tmp
        return tmp

     """
        4
         \
          8
         /
        6
     """   
    def rightLeftRotate(self, node):
        node.right = self.rightRotate(node.right)
        return self.leftRotate(node)
        
    def leftRightRotate(self, node):
        node.left = self.leftRotate(node.left)
        return self.rightRotate(node)
                       
b = BinarySearch()
# b.add(60)
# b.add(12)
# b.add(41)
# b.add(4)
# b.add(29)
# b.add(23)
# b.add(37)
# b.add(1)

# b.remove(b.root, 12)
