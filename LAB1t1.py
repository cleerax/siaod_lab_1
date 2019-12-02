import random

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LOS:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, x):
        self.length += 1
        if self.first == None:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

if __name__ == "__main__":
    zdohnet = LOS()
    s = 0
    b = ""
    for i in range(10):
        zdohnet.add(random.randrange(-99, 100))
    current = zdohnet.first
    for i in range(zdohnet.length):
        if i == zdohnet.length - 2 or i == zdohnet.length - 1:
            s += current.value
        b += str(current.value) + ' '
        current = current.next
    print("Список: {0}".format(b[:-1]))
    print("Сумма двух последних элементов = {0}".format(s))