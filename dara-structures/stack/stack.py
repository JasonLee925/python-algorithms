class Stack():
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        del self.stack[self.size()-1]

    def printAll(self):
        print(self.stack)

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0


stack_instance = Stack()
stack_instance.push('a')
stack_instance.push('b')
stack_instance.push('c')
stack_instance.pop()
stack_instance.printAll()
