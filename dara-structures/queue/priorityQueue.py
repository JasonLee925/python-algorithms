import heapq


class PriorityQueue:
    def __init__(self):
        self.arr = []
        self.index = 0

    def isEmpty(self):
        return len(self.arr) == 0

    def enQueue(self, element, priority):
        heapq.heappush(self.arr, (priority, self.index, element))
        self.index += 1

    def deQueue(self):
        heapq.heappop(self.arr)[-1]

    def printAll(self):
        print(self.arr)


queue_instance = PriorityQueue()

queue_instance.enQueue('a', 1)
queue_instance.enQueue('aaa', 1)
queue_instance.enQueue('b', 3)
queue_instance.enQueue('c', 2)
queue_instance.enQueue('d', 5)
queue_instance.enQueue('e', 4)
queue_instance.printAll()

queue_instance.deQueue()
queue_instance.deQueue()
queue_instance.printAll()
