class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def addRear(self, item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)