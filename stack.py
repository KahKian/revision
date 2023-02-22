class Stack:
    def __init__(self):
        self.top=-1
        self.data=[]
    def push(self,value):
        self.data.append(0)
        self.top += 1
        self.data[self.top] = value
    def pop(self):
        value = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return value
    def printList(self):
        print("\nContent: ")
        for element in self.data:
            print(element, end=' ')


stack = Stack()
stack.push(2)
stack.push(3)
print(stack.printList())
stack.pop()
print(stack.printList())