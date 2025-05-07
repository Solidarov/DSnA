class ArrayQueue:
    def __init__(self, size):
        self.rear = -1
        self.max_size = size
        self.queue = []

    def enqueue(self, value):
        if self.is_full():
            return
        self.queue.append(value)
        self.rear += 1
        return self.queue[self.rear]

    def dequeue(self):
        if self.is_empty():
            return 
        value = self.queue.pop(0)
        self.rear -= 1
        return value

    def peek(self):
        if self.is_empty():
            return
        value = self.queue[0]
        return value

    def is_full(self):
        if self.rear < self.max_size - 1:
            return False
        return True
    
    def is_empty(self):
        if not self.queue or self.rear <= -1:
            return True
        return False
    
    def display(self):
        queue_struct = "\nStructure of the queue:"
        queue_struct += "\nFront -> "
        for i in range(0, self.rear + 1):
            queue_struct += f"{self.queue[i]} -> "
        queue_struct += "Rear"
        return queue_struct