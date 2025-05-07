class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = size

    def enqueue(self, value):
        if self.is_full():
            return
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        return self.rear.data

    def dequeue(self):
        if self.is_empty():
            return
        node = self.front
        self.front = self.front.next
        self.size -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            return 
        value = self.front.data
        return value

    def is_full(self):
        if self.size < self.max_size:
            return False
        return True
    
    def is_empty(self):
        if self.front is None or self.size == 0:
            return True
        return False
    
    def display(self):
        queue_struct = "\nStructure of the queue:"
        queue_struct += "\nFront -> "
        current = self.front
        while current is not None:
            queue_struct += f"{current.data} -> "
            current = current.next
        queue_struct += f"Rear"
        return queue_struct