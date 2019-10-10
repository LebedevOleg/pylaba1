from tkinter import*
import Queue

def click1():
    tempint = txt1.get().split(" ")
    tempint = [int(i) for i in tempint]
    for i in tempint:
        q1.add(i)
    lbl1.configure(text = q1)
    txt1.configure(text = "")
def click2():
    q1.clear()
    lbl1.configure(text=q1)
def click3():
    lbl3.configure(text=q1.task())

q1 = Queue.Queue()
win = Tk()
win.title("Лабараторная 1.3")

txt1 = Entry(win, width = 12)
txt2 = Entry(win, width = 3)
txt1.grid(column= 0, row = 0)
txt2.grid(column = 0,row = 1)

btn1 = Button(win,text = "Добавить в очередь",command = click1)
btn2 = Button(win, text = "Очистить очередь",command = click2)
btn3 = Button(win, text = "Колличество совершенных чисел",command = click3)
btn1.grid(column = 0,row = 1)
btn2.grid(column = 0,row = 2)
btn3.grid(column = 0, row = 3)

lbl1 = Label(win)
lbl2 = Label(win,text = "Введенная очередь:")
lbl3 = Label(win)
lbl1.grid(column = 1, row = 1)
lbl2.grid(column = 1, row = 0)
lbl3.grid(column = 1, row = 3)

win.mainloop()