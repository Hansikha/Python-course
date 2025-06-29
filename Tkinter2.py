from tkinter import *

start = Tk()

start.title("MY FIRST GUI TINKER CODE")

start.geometry("300x300")

l1 = Label(start, text = "Hey There", bg = "pink", fg = "black")

l1.pack()

l2 = Label(start, text = "Full Name", bg = "green", fg = "black")

l2.pack()

e1 = Entry(start)

e1.pack()

t1 = Text(start, height = 50, width = 50)
def click():
  n = e1.get()
  t1.insert(END, n)
def Clear():
  t1.delete(1.0, END)
b1 = Button(start, text="Begin", bg ="blue", fg = "black", command = click)

b1.pack()
b2 = Button(start, text="Clear", bg ="blue", fg = "black", command = Clear)

b2.pack()

t1.pack()

start.mainloop()
