class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def is_empty(self):
        return self.top is None or self.size == 0
    
    def display_top(self):
        if self.is_empty():
            return
        return self.top.data
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return
        current_top = self.top.data
        self.top = self.top.next
        self.size -= 1
        return current_top

    def display(self):
        lls_structure = "Top -> "
        current = self.top
        while current is not None:
            lls_structure += f"{current.data} -> "
            current = current.next
        lls_structure += "End"
        return lls_structure
