class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        address = self.hash(key)
        while self.table[address]:
            address = self.hash(address + 1)
        self.table[address] = key

    def get(self, key):
        address = self.hash(key)
        start = address
        while self.table[address] != key:
            address = self.hash(address + 1)
            if not self.table[address] or address == start:
                return None
        return address

    def remove(self, key):
        start = address = self.hash(key)
        while self.table[address] != key:
            address = self.hash(address + 1)
            if not self.table[address] or address == start:
                return
        self.table[address] = None


H = HashTable(3)
H.insert(5)
H.insert(2)
H.insert(10)
print(H.get(10))

H.remove(10)
print(H.get(10))
print(H.get(2))
print(H.get(5))
