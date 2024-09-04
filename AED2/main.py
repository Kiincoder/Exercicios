from math import floor

class HashTable:
    def __init__(self, size):
        self.size = size + size//2 + 1
        print(self.size)
        self.keys = [None] * self.size
        self.names = [None] * self.size
        self.pointers = [None] * self.size
    
    def hash(self, key):
        return key%self.size + 1

    def insert(self, key, value):
        index = self.hash(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.names[index] = value
        else:
            newIndex = index
            while self.keys[newIndex] != None:
                newIndex += 1
            self.keys[newIndex] = key
            self.names[newIndex] = value
            self.pointers[index] = newIndex


    def print(self):
        # print("Keys", "|", "Nome", "|", "E")
        for i in range(0, self.size):
            if self.keys[i] != None:
                print(i, "|", self.keys[i], "|", self.names[i], "|", self.pointers[i])


table = HashTable(7)
table.insert(73, "João")
table.insert(15, "Carlos")
table.insert(44, "Marcia")
table.insert(37, "Ronaldo")
table.insert(30, "Michel")
table.insert(59, "Darci")
table.insert(61, "Joana")
table.insert(99, "Denise")
table.print()