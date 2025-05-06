
class ArrayStack:
    def __init__(self):
        self.top = -1
        self.size = 0 
        self.stack = list()

    def is_empty(self):
        return self.top == -1 or self.size == 0
    
    def display_top(self):
        if self.is_empty():
            return
        return self.stack[self.top]
    
    def push(self, value):
        self.stack.append(value)
        self.top += 1
        self.size += 1

    def pop(self):
        if self.is_empty():
            return
        value = self.stack.pop(self.top)
        self.top -= 1
        self.size -= 1
        return value

    def display(self):
        stack_structure = "Top -> "
        for i in range(self.top, -1, -1):
            stack_structure += f"{self.stack[i]} -> "
        stack_structure += "End"
        return stack_structure
    


