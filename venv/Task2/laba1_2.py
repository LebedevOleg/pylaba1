from tkinter import*
from tkinter import scrolledtext
import Stack

def click1():
    temp = txt1.get().split()
    for i in temp:
        st1.push(i)
    lbl1.configure(text = st1)
def click2():
    st1.clear()
    lbl1.configure(text=st1)
def click3():
    st2.clear()
    temp = []
    temp = st1.task1()
    if len(temp) == 0:
        lbl3.configure(text = "Нет полиндромов")
    else:
        for i in temp:
            st2.push(i)
        lbl3.configure(text=st2)


st1 =Stack.Stack()
st2 = Stack.Stack()

win = Tk()
win.title("Лабараторная 1.2")

txt1 = Entry(win, width = 12)
txt1.grid(column= 0, row = 0)

btn1 = Button(win,text = "Добавить слово в стек",command = click1)
btn2 = Button(win, text = "Очистить стэк",command = click2)
btn3 = Button(win,text = "Поиск полиндромов", command = click3)
btn1.grid(column = 0,row = 1)
btn2.grid(column = 0,row = 3)
btn3.grid(column = 0,row = 4)

lbl1 = Label(win)
lbl2 = Label(win,text = "Введенный стэк:")
lbl3 = Label(win)
lbl1.grid(column = 1, row = 1)
lbl2.grid(column = 1, row = 0)
lbl3.grid(column = 1, row = 4)

win.mainloop()