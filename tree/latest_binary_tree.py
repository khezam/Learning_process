class Node :
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
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
        
    def add(self, element):
        if not self.root:
            self.root = Node(element)
        else:
            self.addNode(self.root, element)
        self.size += 1
        return self.root
    
    #Finding the min value recursevly
    def minValue(self, curr):
        if not curr:
            return curr
        elif not curr.left:
            return curr.element
        return self.minValue(curr.left)
        
    #Finding the min value recursevly    
    def maxValue(self, curr):
        if not curr:
            return curr
        elif not curr.right:
            return curr.element
        return self.maxValue(curr.right)
    
    #Finding the min value itervely  
    def minValue(self):
        if not self.root:
            return self.root
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.element
        
    #Finding the max value itervely 
    def maxValue(self):
        if not self.root:
            return self.root
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.element
     
    # I tried adding node iteravtly but did not work %100  
    # def add(self, element):
    #     new_node = Node(element)
    #     if not self.root:
    #         self.root = new_node
    #         return self.root
    #     curr = self.root
    #     if not curr.left and curr.element < new_node.element:
    #         curr.right = new_node
    #         return curr
    #     elif not curr.right and curr.element > new_node.element:
    #         curr.left = new_node
    #         return curr
        
    #     while curr.left and curr.right:
    #         if curr.element < new_node.element:
    #             curr = curr.right
    #         else:
    #             curr = curr.left
    #     if not curr.left and curr.element > new_node.element:
    #             curr.left = new_node
    #     else:
    #         curr.right = new_node
            
            
        
    
    
# b = BinaryTree()
# b.add(10)
# b.add(40)
# b.add(5)
# b.add(60)
