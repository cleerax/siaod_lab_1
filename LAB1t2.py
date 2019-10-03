import random

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, a):
        if self.head == None:
            self.head = Node(a)
        else:
            self.head = Node(a, self.head)

    def pop(self):
        if self.head == None:
            return None
        else:
            f = self.head.value
            self.head = self.head.next
            return f

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.value
        

if __name__ == "__main__":
    n = -1
    while n <= 0:
        try:
            n = int(input("Введите длину стека: "))
        except Exception:
            print("Ошибка ввода")
    
    st = Stack()
    s = ""
    for i in range(n):
        st.push(random.randrange(-99, 100))
        s += str(st.peek()) + ' '
    s = s[:-1]
    print("Сформированный стек: {0}".format(s))
    st1 = Stack()
    f = st.peek()
    for i in range(n):
        st1.push(st.pop())
    st = Stack()
    st.push(f)
    s = str(st.peek()) + ' '
    for i in range(n):
        st.push(st1.pop())
        s += str(st.peek()) + ' '
    s = s[:-1]
    del st1
    print("Новый стек: {0}".format(s))