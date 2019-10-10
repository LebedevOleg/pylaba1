from tkinter import*
from tkinter import messagebox
import linklist
#1methods
def click1():
    tempint = txt1.get().split(" ")
    tempint = [int(i) for i in tempint]
    for i in tempint:
        l1.add(i)
    l1.sort()
    messagebox.showinfo("First list", l1)
def click2():
    tempint = txt2.get().split(" ")
    tempint = [int(i) for i in tempint]
    for i in tempint:
        l2.add(i)
    l2.sort()
    messagebox.showinfo("Second list", l2)
def delite1():
    l1.clear()
    messagebox.showinfo("First list", "list 1 clear")
def delite2():
    l2.clear()
    messagebox.showinfo("Second list", "list 2 clear")
def click3():
    l3.clear()
    templist3 = []
    templist1 = l1.createList()
    templist2 = l2.createList()
    templist3 = templist1 + templist2
    for i in templist3:
        l3.add(i)
    l3.sort()
    lbl3.configure(text = l3)


#1methods

l1 = linklist.LinkList()
l2 = linklist.LinkList()
l3 = linklist.LinkList()

window= Tk()
window.title("Лабораторная работа 1.1")
#label
lbl1 = Label(window,text = "Введите элементы первого листа через пробел:")
lbl2 = Label(window,text = "Введите элементы второго листа через пробел:")
lbl3 = Label(window)
lbl2.grid(column = 2,row = 0)
lbl1.grid(column = 0,row = 0)
lbl3.grid(column = 1,row = 3)
#label

#region Button
btn1 =Button(window,text = "Принять список",command = click1)
btn2 =Button(window,text = "Принять список",command = click2)
btn3 = Button(window,text = "Общий список(Задание 1)", command = click3 )
btn4 = Button(window, text = "Очистить лист 1", command = delite1)
btn5 = Button(window, text = "Очистить лист 1", command = delite2)
btn1.grid(column = 0,row = 2)
btn2.grid(column = 2,row = 2)
btn3.grid(column = 1,row = 4)
btn4.grid(column = 0,row = 3)
btn5.grid(column = 2,row = 3)
#endregion Button


#TextBox
txt1 = Entry(window,width =10)
txt2 = Entry(window,width =10)
txt1.grid(column = 0, row = 1)
txt2.grid(column = 2, row = 1)

window.mainloop()