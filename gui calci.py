import numpy as np
import math
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Calci")

root.geometry("400x500")
root.resizable()

e=Entry(root,width=50,borderwidth=5)
e.grid(row=0, column=0, columnspan=30, padx=10, pady=10)
def a(num):
    fuh=e.get()
    e.delete(0, END)
    e.insert(0, str(fuh)+str(num))
    return

def add():
    global solv
    first_num=e.get()
    solv=float(first_num)
    e.delete(0, END)
    global var
    var=1
    return
def sub():
    global solv
    first_num=e.get()
    solv=float(first_num)
    e.delete(0, END)
    global var
    var=2
    return
def mul():
    global solv
    first_num = e.get()
    solv = float(first_num)
    e.delete(0, END)
    global var
    var = 3
    return
def div():
    global solv
    first_num = e.get()
    solv = float(first_num)
    e.delete(0, END)
    global var
    var = 4
    return
def log():
    global solv
    num =e.get()
    e.delete(0, END)
    solv=float(num)
    e.insert(0,"ln")
    global var
    var = 5
    return
def sin():
    global solv
    num = e.get()
    e.delete(0, END)
    solv = float(num)
    e.insert(0, "Sin")
    global var
    var = 6
    return
def cos():
    global solv
    num = e.get()
    e.delete(0, END)
    solv = float(num)
    e.insert(0, "Cos")
    global var
    var = 7
    return
def exp():
    global solv
    num = e.get()
    e.delete(0, END)
    solv = float(num)
    e.insert(0, "Exp")
    global var
    var = 8
    return
def dot():
    return
def delt():
    num=e.get()
    num1=float(num)/10
    e.delete(0,END)
    e.insert(0,float(num1))
    return
def rem():
    e.delete(0, END)
    return
def eq():
    if(var==1):
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, solv + float(second_num))
    if(var==2):
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, solv - float(second_num))
    if (var == 3):
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, solv * float(second_num))
    if (var == 4):
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, solv / float(second_num))
    if(var==5):
        e.delete(0,END)
        num=math.log(solv,2.7)
        e.insert(0, num)
    if(var==6):
        e.delete(0,END)
        num=np.sin(solv)
        e.insert(0,num)
    if (var == 7):
        e.delete(0, END)
        num = np.cos(solv)
        e.insert(0, num)
    if (var == 8):
        e.delete(0, END)
        num = math.pow(2.7,solv)
        e.insert(0, num)

    return


button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: a('1'))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: a('2'))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: a(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda:a(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda:a(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda:a(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda:a(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda:a(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda:a(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda:a(0))
button_10 = tk.Button(root, text="+" , padx=40, pady=20,bg="red",command=add)
button_11 = tk.Button(root, text="-", padx=40, pady=20, command=sub)
button_12 = tk.Button(root, text="*", padx=40, pady=20, command=mul)
button_13 = tk.Button(root, text="/", padx=40, pady=20, command=div)
button_14 = tk.Button(root, text="sin", padx=40, pady=20, command=sin)
button_15 = tk.Button(root, text="cos", padx=40, pady=20, command=cos)
button_16 = tk.Button(root, text="ln", padx=40, pady=20, command=log)
button_17 = tk.Button(root, text="e", padx=40, pady=20, command=exp)
button_18 = tk.Button(root, text="=", padx=40, pady=20, command=eq)
button_19= tk.Button(root, text="del", padx=40, pady=20, command=delt)
button_20 = tk.Button(root, text="C", padx=40, pady=20, command=rem)
button_21= tk.Button(root, text=".", padx=40, pady=20, command=lambda: a("."))


button_0.grid(row=4, column=0)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_10.grid(row=2, column=3)
button_11.grid(row=3, column=3)
button_12.grid(row=4, column=2)
button_13.grid(row=4, column=3)
button_14.grid(row=5, column=0)
button_15.grid(row=5, column=1)
button_16.grid(row=6, column=0)
button_17.grid(row=5, column=2)
button_18.grid(row=6, column=2)
button_19.grid(row=5, column=3)
button_20.grid(row=1, column=3)
button_21 .grid(row=4, column=1)

root.mainloop()
