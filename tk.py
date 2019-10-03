from tkinter import *
import tkinter.ttk as ttk
from LAB1t1 import Node, LOS
from LAB1t2 import Stack
from LAB1t3 import Queue

import random

def task1():
    try:
        n = int(txt1.get())
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
        lbl12.config(text = ("Список\r\n{0}".format(b[:-1])))
        lbl13.config(text = ("Сумма двух последних элементов\r\n{0}".format(s)))
    except Exception:
        txt1.delete(0, END)
        lbl12.config(text = "ВВЕДЕНА НЕПРАВИЛЬНАЯ ДЛИНА СПИСКА")
        lbl13.config(text = '')

def task2():
    try:
        n = int(txt2.get())
        st = Stack()
        s = ""
        for i in range(n):
            st.push(random.randrange(-99, 100))
            s += str(st.peek()) + ' '
        s = s[:-1]
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
        lbl23.config(text = ("Новый стек\r\n{0}".format(s)))
    except Exception:
        txt2.delete(0, END)
        lbl22.config(text = "ВВЕДЕНА НЕПРАВИЛЬНАЯ ДЛИНА СТЕКА")
        lbl23.config(text = '')

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

tab_control.pack(expand = 1, fill = "both") 
window.mainloop()