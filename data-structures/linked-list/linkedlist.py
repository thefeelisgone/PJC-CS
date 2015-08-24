from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, new_data):
        """Add a new node to the front of the list."""
        new_node = Node(new_data)
        new_node.setPtr(self.head)
        self.head = new_node

    def append(self, new_data):
        """Add a new node to the end of the list."""
        new_node = Node(new_data)
        current = self.head

        if current is None:
            self.head = new_node
        else:
            while current.getPtr() is not None:
                current = current.getPtr()

            current.setPtr(new_node)

    def pop(self):
        """Remove the node at the end of the list and return its data."""
        current = self.head
        prev = None

        while current.getPtr() is not None:
            prev = current
            current = current.getPtr()

        if prev is None:
            self.head = None
        else:
            prev.setPtr(None)

        return current.getData()
    
    def remove_first(self):
        """Remove the node at the start of the list and return its data, False otherwise."""
        if self.head is None:
            return False
        else:
            value = self.head.getData()
            self.head = self.head.getPtr()
            return value
            

    def isEmpty(self):
        """Return True if the list is empty, False otherwise."""
        return self.head is None

    def size(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head

        while current is not None:
            current = current.getPtr()
            count += 1

        return count
        
    def search(self,search_data):
        """Returns the position of the node that contains the data, False otherwise"""
        if self.isEmpty is True:
            return False
        else:
            current = self.head
            count = 0
            
            while current.getData() is not search_data:
                if current.getPtr() is None:
                    return False
                else:
                    current = current.getPtr()
                    
            return current.getData()
