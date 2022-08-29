


# -----------------------
# Addtional methods
# -----------------------

# clear() - Remove all nodes in the linked list
# delete/pop(index) - Remove a node
# get(index) - Get the data at the specified position
# Others as your code needs

# -------------------------------------------------------------------------------------------------------------------------------------
# Linked List (singly)
# -------------------------------------------------------------------------------------------------------------------------------------

class LinkedList:
    def __init__(self):
        self.head =None
        self.tail= None
        self.size = 0
        
# Length of Linked List (N of 1)
    def length(self):
        current = self.head
        count = 0 
        while current != None:
            count +=1  
            current = current.get_next_node()
        return count

# Length of Linked List (0 of 1)
    def length1(self):
        return self.size
    
test = LinkedList()
print(test)
# -------------------------------------------------------------------------------------------------------------------------------------
# Linked List (Doubly Linked Node)
# -------------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data=None) :
        self.data = data
        self.next = None
        self.prev = None
        
    def set_next_node(self, node):
        self.next = node
        
    def get_next_node(self):
        return self.next
    
    def set_prev_node(self, node):
        self.prev = node
        
    def get_prev_node(self):
        return self.prev