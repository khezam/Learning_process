class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
        
        
    def traverse_left(self, new_node):
        curr = self.root
        while curr.left:
            curr = curr.left
        curr.left = new_node
        return  curr
        
    def traverse_right(self, new_node):
        curr = self.root
        while curr.right:
            curr = curr.right
        curr.right = new_node
        return curr
        
    def append_left(self, element):
        new_node = Node(element)
        if not self.root:
            self.root = new_node
            return self.root
        else:
            return self.traverse_left(new_node)
            
    def append_right(self, element):
        new_node = Node(element)
        if not self.root:
            self.root = new_node
            return self.root
        else:
            return self.traverse_right(new_node)
            
    def preorderTrav(self, binary_tree):
        if binary_tree:
            print(self.preorderTrav(binary_tree.left))
            print(binary_tree.element)
        

b = BinaryTree()
# b.append_left("A")
# b.append_right("B")
# b.append_left("C")
# b.append_right("D")
# b.append_left("E")
# b.preorderTrav(b.root)


