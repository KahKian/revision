class Queue:
    def __init__(self):
        self.rear = -1
        self.data = []

    def enqueue(self, value):
        self.rear += 1
        self.data.append(value)

    def dequeue(self):
        value = self.data[0]
        del self.data[0]
        self.rear -= 1
        return value

    def printList(self):
        print("\nCurrent list: ")
        for element in self.data:
            print(element, end=' ')

queue = Queue()
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)
queue.printList()
queue.dequeue()
queue.printList()
