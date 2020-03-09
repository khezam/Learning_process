# class Node:
#     def __init__(self, element):
#         self.element = element 
#         self.left = None
#         self.right = None
        
# class BTree:
#     def __init__(self):
#         self.root = None
        
        
#     def addNode(self, new_node, node):
#         if new_node.element > node.element:
#             """Base case if node.rigth == None"""
#             if node.right == None:
#                 node.right = new_node
#             else:
#                 """Recursivly call the function and pass a right reference"""
#                 return self.addNode(new_node, node.right)
                
#         else: 
#             """Base case if node.right == None"""
#             if node.left == None:
#                 node.left = new_node
#             else:
#                 """Recursivly call the function and pass a left reference"""
#                 return self.addNode(new_node, node.left)
       
#     def add(self, element):
#         """This function creat a root if the Tree is empty"""
#         if not self.root:
#             self.root = Node(element)
#         else:
#             """If root is not empty then call addNode funciton"""
#             self.addNode(Node(element), self.root)
            

class Node:
    def __init__(self, element):
        self.element = element 
        self.left = None
        self.right = None
        
class BTree:
    def __init__(self):
        self.root = None
        
        
    def addNode(self, element, node):
        if element > node.element:
            if node.right == None:
                node.right = Node(element)
            else:
                return self.addNode(element, node.right)      
        else: 
            if node.left == None:
                node.left = Node(element)
            else:
                return self.addNode(element, node.left)
       
    def add(self, element):
        if not self.root:
            self.root = Node(element)
        else:
            self.addNode(element, self.root)
            

b = BTree()
