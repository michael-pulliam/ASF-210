
# ------------------------------------------------------------------------------------------------------------------------------
# Node
# ------------------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data=None) :
        self.data = data
        self.next = None
        self.prev = None
    
    def set_next_node(self, node):
        self.next = node
        
    def get_next_node(self):
        return self.next
    
    def __str__(self):
        return str(self.data)
    
x = "Happy"
y = "Birthday"

node1 = Node(x)
node2 = Node(y)

node1.set_next_node(node2)

print(node1)
print(node1.get_next_node())