from tkinter import *

window = Tk()
window.title("Event Handling")
window.geometry("100x100")

def handle_keypress(event):
  print("Key pressed: ", event.char)
  
def button_press(event):
  print("Button has been clicked")
  
window.bind("<Key>", handle_keypress)
b1 = Button(window, text = "click me!!")
b1.pack()

b1.bind("<Button-1>", button_press)
window.mainloop()
