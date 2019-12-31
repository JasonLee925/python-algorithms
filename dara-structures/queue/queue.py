class Queue:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0

    def enQueue(self, element):
        self.arr.append(element)

    def deQueue(self):
        del self.arr[0]

    def front(self):
        return self.arr[0]

    def last(self):
        return self.arr[len(self.arr) - 1]

    def printAll(self):
        print(self.arr)

    def size(self):
        return len(self.arr)

    def clear(self):
        return self.arr.clear()


queue_instance = Queue()
print(queue_instance.isEmpty())
queue_instance.enQueue('a')
queue_instance.enQueue('b')
queue_instance.enQueue('c')
queue_instance.enQueue('d')
queue_instance.deQueue()
queue_instance.deQueue()
queue_instance.printAll()
print(queue_instance.size())
