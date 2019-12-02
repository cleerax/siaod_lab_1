import random

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.prev = next

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        if self.first == None:
            self.first = Node(item)
        elif self.first.prev == None:
            self.last = Node(item)
            self.first.prev = self.last
        else:
            t = Node(item)
            self.last.prev = t
            self.last = t
            del t

    def dequeue(self):
        if self.first == None:
            return None
        elif self.first.prev == None:
            res = self.first.value
            self.first = None
            self.last = None
            return res
        else:
            res = self.first.value
            i = self.first
            while (i != None and i.prev != None):
                i.value = i.prev.value
                if i.prev.prev == None:
                    i.prev = None
                i = i.prev
            return res


    def top(self):
        return self.first.value

    def size(self):
        i = self.first
        res = 0
        while (i != None and i.prev != None):
            i = i.prev
            res += 1
        if self.last != None:
            res += 1
        return res

    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False

    def __str__(self):
        s = ""
        i = self.first
        while (i != None and i.prev != None):
            s += str(i.value) + ' '
            i = i.prev
        if i != None:
            s += str(i.value)
        return s

if __name__ == "__main__":
    q = Queue()
    s = ""
    for i in range(10):
        q.enqueue(random.randrange(-99, 100))
    print(str(q) + ", размер = ", str(q.size()))

    for i in range(10):
        s += str(q.dequeue()) + ' '
    print(s)

    print(str(q) + ", размер = ", str(q.size()))

    print(str(q.isEmpty()))