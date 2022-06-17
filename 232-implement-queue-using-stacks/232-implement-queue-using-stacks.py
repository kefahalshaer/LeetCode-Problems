class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class MyQueue:

    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def push(self, x: int) -> None:
        self.left.push(x)

    def pop(self) -> int:
        if self.right.isEmpty():
            while not self.left.isEmpty():
                self.right.push(self.left.pop())
    
        return self.right.pop()

    def peek(self) -> int:
        if self.right.isEmpty():
            while not self.left.isEmpty():
                self.right.push(self.left.pop())
        temp = self.right.pop()
        self.right.push(temp)
        return temp
            
        return temp

    def empty(self) -> bool:
        return self.right.isEmpty() and self.left.isEmpty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()