from tkinter import*
from subprocess import Popen
import sys

def click1():
    subprocess.Popen([sys.executable, 'laba1'])
def click2():
    subprocess.Popen([sys.executable, 'laba1_2'])
def click3():
    subprocess.Popen([sys.executable, 'laba1_3'])

window= Tk()
window.title("Лабораторная работа 1")

btn1 =Button(window,text = "Задание 1",command = click1)
btn2 =Button(window,text = "Задание 2",command = click2)
btn3 = Button(window,text = "Задание 3",command = click3)
btn1.grid(column = 0, row = 0)
btn2.grid(column = 0, row = 1)
btn3.grid(column = 0, row = 2)
window.mainloop()