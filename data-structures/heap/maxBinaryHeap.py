class MaxHeap:
    def __init__(self, capacity=10):
        self._default = object()
        self.capacity = capacity
        self.heap = [self._default] * self.capacity

    def __getitem__(self, i):
        return self.heap[i]

    def __len__(self):
        return len(self.heap) - self.heap.count(self._default)

    def insert(self, item):
        self.heap[len(self)] = item
        self.fixUp(self.heap.index(item))

    def getParent(self, i):
        return (i-1)/2

    def fixUp(self, i):
        if i > 0 and self.heap[i] > self.heap[self.getParent(i)]:
            self.swap(i, self.getParent(i))
            self.fixUp(self.getParent(i))

    def fixDown(self, i):
        parent = self.heap[i]
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        largest_index = i
        if left_index < len(self) and self.heap[left_index] > parent:
            largest_index = left_index
        if right_index < len(self) and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index
        if i != largest_index:
            self.swap(i, largest_index)
            self.fixDown(largest_index)

    def poll(self):
        max_ = self.max_
        self.swap(0, len(self) - 1)
        self.heap[len(self) - 1] = self._default
        self.fixDown(0)
        return max_

    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    @property
    def max_(self):
        return self.heap[0]


myHeap = MaxHeap()
myHeap.insert(1)
myHeap.insert(3)
myHeap.insert(6)
myHeap.insert(5)
myHeap.insert(9)
myHeap.insert(8)

for h in myHeap:
    print(h)

print('------------------------------------------')
myHeap.poll()

for h in myHeap:
    print(h)
