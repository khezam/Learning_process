class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        return self.head
        
    def length(self, curr, i):
        if curr == None:
            return i
        return self.length(curr.next, i + 1)
        
    def splitNodes(self, linked_list, curr, mid, i):
        if i != mid:
            return self.splitNodes(linked_list, curr.next, mid, i + 1)
        left = linked_list
        right = curr.next
        curr.next = None

        return left, right
    
    def mergeSort(self, linked_list):
        if linked_list.next == None:
            return linked_list
        mid = (self.length(linked_list, 0) // 2) - 1
        leftHalf, rightHalf = self.splitNodes(linked_list, linked_list, mid, 0)
        left = self.mergeSort(leftHalf)
        right = self.mergeSort(rightHalf)
        
        return self.merge(left, right)
        
    def merge(self, left, right):
        sorted = LinkedList()
        currLeft = left
        currRight = right
        
        while currLeft and currRight:
            if currLeft.element < currRight.element:
                if not sorted.head:
                    sorted.head = currLeft
                else:
                    sorted.tail.next = currLeft
                sorted.tail = currLeft
                currLeft = currLeft.next
            else:
                if not sorted.head:
                    sorted.head = currRight
                else:
                    sorted.tail.next = currRight
                sorted.tail = currRight
                currRight = currRight.next
                
        if currLeft:
            sorted.tail.next = currLeft
            sorted.tail = currLeft
        else:
            sorted.tail.next = currRight
            sorted.tail = currRight
            
        return sorted.head
              
l = LinkedList()
# l.append(1000)
# l.append(-10)
# l.append(-1000)
# l.append(500)
# l.append(200)
# l.append(5)
# l.append(0)


# sort = l.mergeSort(l.head)
# l.head, l.tail = sort, None 