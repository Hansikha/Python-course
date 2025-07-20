from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.geometry("200x200")

def msg():
  messagebox.showwarning("ALERT!", "A VIRUS HAS BEEN DETECTED!!")

b1 = Button(root, text = "Scan for viruses", command = msg)
b1.pack()
root.mainloop()
