class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def addNode(self, node, element):
        if node.element < element:
            if not node.right:
                node.right = Node(element)
            else:
                return self.addNode(node.right, element)
        else:
            if not node.left:
                node.left = Node(element)
            else:
                return self.addNode(node.left, element)
        
    def add(self, element):
        if not self.root:
            self.root = Node(element)
            return self.root
        else:
            return self.addNode(self.root, element)
            
    def search(self, node, target):
        if not node:
            return False
        elif node.element == target:
            return node.element
        elif node.element < target:
            return self.search(node.right, target)
        else:
            return self.search(node.left,  target)
            
    def minValue(self, node):
        if not node:
            return node
        elif not node.left:
            return node.element
        return self.minValue(node.left)
        
    def maxValue(self, node):
        if not node:
            return node
        elif node.right:
            return node.element
        return self.maxValue(node.right)
    
    def secondLargetValue(self, node):
        if not node.right:
            return node.element
        elif node.right.right:
            return node.element
        return self.secondLargetValue(node.right)
        
        
    def secondSmallestValue(self, node):
        if not node.left:
            return node.element
        elif not node.left.left:
            return node.element
        return self.secondSmallestValue(node.left)
        
    def height(self, node):
        if not node:
            return -1
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            return max(left, right) + 1
            
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
            
    def size(self, node):
        if not node:
            return 0
        else:
            left = self.size(node.left)
            right = self.size(node.right)
            
            return (left + right) + 1
        
    def traverseLeft(self, curr):
        if not curr.left:
            return curr.element
        while curr.left.left:
            curr = curr.left
        successor = curr.left.element
        curr.left = None
        return successor
        
    def remove(self, node, target):
        if not node:
            return node
        elif node.element == target:
            if not node.left and not node.right:
                return None
            elif node.left and node.right:
                node.element = self.traverseLeft(node)
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
            


b = BinaryTree()
# b.add(60)
# b.add(12)
# b.add(4)
# b.add(1)
# b.add(41)
# b.add(29)
# b.add(23)
# b.add(37)
# b.add(42)
# b.remove(b.root, 29)


