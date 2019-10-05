from tkinter import *
import tkinter.ttk as ttk
from LAB1t1 import Node, LOS
from LAB1t2 import Stack
from LAB1t3 import Queue

import random

def task1():
    try:
        n = int(txt1.get())
        if n == 0:
            raise Exception
        zdohnet = LOS()
        s = 0
        b = ""
        for i in range(n):
            zdohnet.add(random.randrange(-99, 100))
        current = zdohnet.first
        for i in range(zdohnet.length):
            if i == zdohnet.length - 2 or i == zdohnet.length - 1:
                s += current.value
            b += str(current.value) + ' '
            current = current.next
        lbl12.grid()
        lbl13.grid()
        lbl12.config(text = ("Список\r\n{0}".format(b[:-1])))
        lbl13.config(text = ("Сумма двух последних элементов\r\n{0}".format(s)))
    except Exception:
        txt1.delete(0, END)
        lbl12.grid()
        lbl13.grid_remove()
        lbl12.config(text = "ВВЕДЕНА НЕПРАВИЛЬНАЯ ДЛИНА СПИСКА")
        lbl13.config(text = '')

def task2():
    try:
        n = int(txt2.get())
        if n == 0:
            raise Exception
        st = Stack()
        s = ""
        for i in range(n):
            st.push(random.randrange(-99, 100))
            s += str(st.peek()) + ' '
        s = s[:-1]
        lbl22.grid()
        lbl22.config(text = ("Сформированный стек\r\n{0}".format(s)))
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
        lbl23.grid()
        lbl23.config(text = ("Новый стек\r\n{0}".format(s)))
    except Exception:
        txt2.delete(0, END)
        lbl22.grid()
        lbl23.grid_remove()
        lbl22.config(text = "ВВЕДЕНА НЕПРАВИЛЬНАЯ ДЛИНА СТЕКА")
        lbl23.config(text = '')

def radio():
    if var.get() == 0:
        lbl32.grid_remove()
        txt32.grid_remove()
    if var.get() == 1:
        lbl32.grid()
        txt32.grid()
    lbl33.grid_remove()

def task3():
    try:
        q = Queue()
        n = int(txt31.get())
        if n == 0:
            raise Exception("Очередь не может быть пустой")

        if var.get() == 0:
            for i in range(n):
                q.enqueue(random.randrange(-99, 100))
        
        if var.get() == 1:
            s = str(txt32.get())
            arr = list(map(int, s.split()))
            if len(arr) == 0:
                raise Exception("Очередь не может быть пустой")
            elif len(arr) > n:
                raise Exception("Переполнение очереди")
            for i in range(n):
                q.enqueue(arr[i])

        lbl33.grid()
        lbl33.config(text = ("Сформированная очередь:\r\n{0}").format(str(q)))
    except Exception as e:
        lbl33.grid()
        lbl33.config(text = "ошибка " + str(e))

window = Tk()
window.title("Лабораторная работа №1")
window.geometry("650x500+350+100")

tab_control = ttk.Notebook()
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Задание 1")
tab_control.add(tab2, text = "Задание 2")
tab_control.add(tab3, text = "Задание 3")

btn1 = Button(tab1, text = "Выполнить задание 1", command = task1)
lbl11 = Label(tab1, text = "Длина списка: ")
lbl12 = Label(tab1, wraplength = 200)
lbl13 = Label(tab1, wraplength = 200)
txt1 = Entry(tab1)
lbl11.grid(column = 0, row = 0)
txt1.grid(column = 1, row = 0)
btn1.grid(column = 1, row = 1, pady = 10)
lbl12.grid(column = 1, row = 2)
lbl13.grid(column = 1, row = 3, pady = 10)
lbl12.grid_remove()
lbl13.grid_remove()

btn2 = Button(tab2, text = "Выполнить задание 2", command = task2)
lbl21 = Label(tab2, text = "Длина стека: ")
lbl22 = Label(tab2, wraplength = 200)
lbl23 = Label(tab2, wraplength = 200)
txt2 = Entry(tab2)
lbl21.grid(column = 0, row = 0)
txt2.grid(column = 1, row = 0)
btn2.grid(column = 1, row = 1, pady = 10)
lbl22.grid(column = 1, row = 2)
lbl23.grid(column = 1, row = 3, pady = 10)
lbl22.grid_remove()
lbl23.grid_remove()

var = BooleanVar()
var.set(0)

lbl31 = Label(tab3, text = "Длина очереди: ")
txt31 = Entry(tab3)
r1 = Radiobutton(tab3, text = "Заполнить очередь случайными числами", variable = var, value = 0, command = radio)
r2 = Radiobutton(tab3, text = "Заполнить вручную", variable = var, value = 1, command = radio)
lbl32 = Label(tab3, text = "Введите очередь")
txt32 = Entry(tab3)
btn3 = Button(tab3, text = "Заполнить очередь", command = task3)
lbl33 = Label(tab3, wraplength = 200)

lbl31.grid(column = 0, row = 0)
txt31.grid(column = 1, row = 0)
r1.grid(column = 1, row = 1)
r2.grid(column = 1, row = 2)
lbl32.grid(column = 0, row = 3)
lbl32.grid_remove()
txt32.grid(column = 1, row = 3)
txt32.grid_remove()
btn3.grid(column = 1, row = 4)
lbl33.grid(column = 1, row = 5)
lbl33.grid_remove

tab_control.pack(expand = 1, fill = "both") 
window.mainloop()