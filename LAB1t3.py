class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def top(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

if __name__ == "__main__":
    q = Queue()