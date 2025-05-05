class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f"Single Linked List Node ({self.data})"

class DLLNode(LLNode):
    def __init__(self, data):
        self.prev = None
        super().__init__(data)

    def __str__(self):
        return f"Double Linked List Node ({self.data})"


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_start(self, data):
        new_node = LLNode(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = LLNode(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def search(self, data):
        if self.head is None:
            return
        current = self.head
        idx = 0

        while current is not None:
            if current.data == data:
                return idx
            current = current.next
            idx += 1

        return

    def delete(self):
        while self.head is not None:
            next = self.head.next
            del self.head
            self.head = next
        self.tail = None
        self.size = 0
        return True

    def delete_at(self, idx):
        if self.head is None:
            return 
        
        if idx >= self.size or idx < 0:
            return
        
        if idx == 0:
            current = self.head
            self.head = current.next
            if self.head is None:
                self.tail = None
            del current
            self.size -= 1
            return True
            
        i = 0
        current = self.head
        while current is not None and current.next is not None and (i + 1) != idx:
            current = current.next
            i += 1
        if current is not None and current.next is not None:
            self.size -= 1
            current.next = current.next.next
            return True
        else:
            return

    def display_forward(self):
        current = self.head
        ll_structure = "Elements of linked list:\nHead -> "
        while current is not None:
            ll_structure += f"{current.data} -> "
            current = current.next
        ll_structure += "Null"
        return ll_structure


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_start(self, data):
        new_node = DLLNode(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = DLLNode(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def search(self, data):
        if self.head is None:
            return
        current = self.head
        idx = 0
        while current is not None:
            if current.data == data:
                return idx
            current = current.next
            idx += 1
        
        return

    def delete(self):
        while self.head is not None:
            next = self.head.next
            del self.head
            self.head = next
        self.tail = None
        self.size = 0

    def delete_at(self, idx):
        if self.head is None:
            return
        if idx < 0 or idx >= self.size:
            return
        
        if idx == 0:
            current = self.head
            self.head = current.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            del current
            self.size -= 1
            return True

        i = 0
        current = self.head
        while current is not None and i < idx:
            current = current.next
            i += 1

        if current is None:
            return
        current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        del current
        self.size -= 1
        return True

    def display_forward(self):
        current = self.head
        dll_structure = "Elements of double linked list:\nHead <--> "
        while current is not None:
            dll_structure += f"{current.data} <--> "
            current = current.next
        dll_structure += "Null"
        return dll_structure

    def display_backward(self):
        current = self.tail
        dll_structure = "Elements of double linked list (backward):\nNull <--> "
        while current is not None:
            dll_structure += f"{current.data} <--> "
            current = current.prev
        dll_structure += "Head"
        return dll_structure
