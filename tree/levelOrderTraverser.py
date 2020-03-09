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
            
    def height(self, node):
        if not node:
            return -1
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            return max(left, right) + 1
            
    def numOfItems(self):
        h = self.height(self.root)
        result = 0
        i = 0
        while i <= h:
            result += 2 ** i
            i += 1
        return result
              
    # def  breadth_traversal(self):
    #     q = Queue()
    #     q.enqueue(self.root)
    #     lst = [None] * self.numOfItems()
    #     size = len(lst) - 1
    #     i = 0
        
    #     while not q.isEmpty():
    #         node = q.dequeue()
    #         if node:
    #             lst[i] = node.element
    #             i += 1
    #         else:
    #             lst[i] = node
    #             i +=1
    #             continue
    #         if node or not node:
    #             if node.left:
    #                 q.enqueue(node.left)
    #             else:
    #                 left = (2*i-1) + 1
    #                 if left < size:
    #                     q.enqueue(node.left)
    #         if node or not node:
    #             if node.right:
    #                 q.enqueue(node.right)
    #             else:
    #                 right = (2*i-1)+2
    #                 if right < size:
    #                     q.enqueue(node.right)
                
    #     return lst

    """A cleaner version of the function above"""
    def  breadth_traversal(self):
        q = Queue()
        q.enqueue(self.root)
        lst = [None] * self.numOfItems()
        size = len(lst) - 1
        i = 0
        
        while not q.isEmpty():
            node = q.dequeue()
            if node:
                lst[i] = node.element
                i += 1
                if node.left:
                    q.enqueue(node.left)
                else:
                    left = (2*i-1) + 1
                    if left < size:
                        q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)
                else:
                    right = (2*i-1) + 2
                    if right < size:
                        q.enqueue(node.right)
            else:
                lst[i] = node
                i +=1
        return lst


def build_tree(elms):
    array = [None] * len(elms)
    n = len(array) - 1

    for i, elm in enumerate(elms):
        if elm:
            new_node = Node(elm)
            array[i] = new_node

    for i, node in enumerate(array):
        if node:
            left = (i*2) + 1
            right = (i*2) + 2
            if left <= n:
                node.left = array[left]
            if right <= n:
                node.right = array[right]

    return array[0] 


def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print(node.element)
    in_order(node.right)


def height(node):
    if not node:
        return 0
    else:
        left = height(node.left)
        right = height(node.right)
        return max(left, right) + 1

def tree_to_array(root):
    import math

    h = height(root)
    arr_size = 2 ** h - 1

    nodes = [None] * arr_size
    nodes[0] = root

    for i in range(1, arr_size):

        is_left = i % 2 == 1

        if is_left:
            parent_index = (i - 1) // 2
            parent = nodes[parent_index]
            if parent:
                nodes[i] = parent.left
        else:
            parent_index = (i - 2) // 2
            parent = nodes[parent_index]
            if parent:
                nodes[i] = parent.right

        """
        parent_index = math.ceil(i / 2) - 1
        parent = nodes[parent_index]
        is_left = i % 2 == 1   # Is an odd number

        if parent:
            if is_left:
                nodes[i] = parent.left
            else:
                nodes[i] = parent.right
        """

    # return [(node.element if node else None) for node in nodes]

    values = []
    for node in nodes:
        if node:
            values.append(node.element)
        else:
            values.append(None)

    return values
            
b = BinaryTree()
b.add(4)
b.add(2)
b.add(6)
b.add(0)
b.add(3)
t = build_tree([4,1,5, None, None, 20, 40])
t = build_tree([4,1,5, 0.5, None, 20, 40, 0.1, -1])
t = build_tree([1, None, 2, None, None, None, 3])

# print(in_order(t))

print(tree_to_array(t))



