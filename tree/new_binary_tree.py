class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def add(self, element):
        if not self.root:
            self.root = Node(element)
        else:
            self.addNode(element, self.root)
        self.size += 1
        return self.root
        
    def addNode(self, element, root):
        if element < root.element:
            if root.left == None:
                root.left = Node(element)
                return self.root
            else:
                return self.addNode(element, root.left)
        else:
            if root.right == None:
                root.right = Node(element)
                return self.root
            else:
                return self.addNode(element, root.right)
                
    def search(self, root, target):
        if root:
            if root.element == target:
                return root.element
            elif root.element > target:
                return self.search(root.left, target)
            else:
                return self.search(root.right, target)
        else:
            return "Not Found"
            
    def binary_search(self, target):
        if self.root:
            return self.search(self.root, target)
        else:
            return "Tree is empty"
            
    # def traverse(self, curr, node):
    #     if not node.left:
    #         node.left = curr
    #         return node
    #     else:
    #         self.traverse(curr, node.left)
    #         return node

    """The function remove() removes a node at a given target key(value).
        Note: When doing so, it increases the height of the tree which makes it less efficient! 
    """
    # def remove(self, node, target):
    #     if not node:
    #         return None 
    #     elif node.element == target:
    #         if not node.left and not node.right:
    #             return None
    #         elif node.left and node.right:
    #             curr = node.left
    #             node = node.right
    #             # The function below traverses all the way to the left of a subtree
    #             self.traverse(curr, node)
    #             return node
    #         else: 
    #             if node.left:
    #                 return node.left
    #             else:
    #                 return node.right
                
    #     elif node.element < target:
    #         node.right = self.remove(node.right, target) 
    #         return node
    #     else:
    #         node.left = self.remove(node.left, target)
    #         return node


    """The functions remove() and traverse() delete a node that has two children by finding the successor of 
        targeted node and set the trageted node element to equal the successor element.
        Note:This approach does NOT change the height of the tree.
    """
    def traverse(self, currLeft):
        # if currLeft.left == None then the successort is currLeft element
        if not currLeft.left:
            return currLeft.element
        while currLeft.left.left:
            currLeft = currLeft.left
        successor = currLeft.left.element 
        currLeft.left = None
        return successor
    
    def remove(self, node, target):
        if not node:
            return None 
        elif node.element == target:
            if not node.left and not node.right:
                return None
            elif node.left and node.right:
                currRight = node.right
                node.element = self.traverse(currRight)
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
# b.add(20)
# b.add(30)
# b.add(35)
# b.add(36)
# b.add(37)
# b.add(35.5)
# b.add(25)
# b.add(23)
# b.add(22)
# b.add(24)
# b.remove(b.root, 25)
