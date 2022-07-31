

class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = node
            self.head = node
        self.count += 1
        

 


    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current
        self.count += 1   
            

  

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        node = Node(data)
        if index < 0:
            print('Error')
        elif index == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.count += 1
        else:
            current = self.head
            for i in range(1, index -1 ):
                if current is not None:
                    current = current.next
            if current is not None:
                node.next = current.next
                node.prev = current
                current.next = node
                self.count += 1
            else:
                print("Index is out of range")

    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1      
        current = self.head
        found = 0
        index = 1
        if current is not None:
            while current is not None:
                index += 1
                if current.data == data:
                    found += 1
                    break
                current = current.next
            if found == 1:
                print(index)
            else:
                print('Item not found')
        else:
            print("list is empty")
            



    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

words = DoublyLinkedList()
words.addFirst('May')
words.add('the')
words.add('Force')
words.add('be')
words.add('with')
words.add('you')
words.addLast('!')
print(words)
words.indexOf('with')
words.__setitem__(5, 'us')
words.addAtIndex('all', 7)
print(words)




