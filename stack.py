class Stack:

    def __init__(self):
        self.capacity = 2
        self.stack = [None] * self.capacity
        self.top = 0

    def push(self, item):
        if self.top == self.capacity:
            self.resize(self.capacity * 2)
        self.stack[self.top] = item
        self.top += 1
        
    def pop(self):
        if self.isEmpty():
            return None
        self.top -= 1
        item = self.stack[self.top]
        self.stack[self.top] = None
        if self.top > 0 and self.top <= self.capacity // 4 and self.capacity > 4:
          self.resize(self.capacity // 2)  
        return item

    def show(self):
        return self.stack[:self.top]
    
    def isEmpty(self):
        return self.top == 0

    def size(self):
        return self.top

    def resize(self, new_capacity):
        new_stack = [None] * new_capacity
        for i in range(self.top):
            new_stack[i] = self.stack[i]
        self.stack = new_stack
        self.capacity = new_capacity