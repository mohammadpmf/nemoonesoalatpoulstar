# Q 2
# from tkinter import *
# def inc():
#     global counter
#     counter += counter
#     if counter < 100:
#         btn.config(text=counter)
# counter = 1
# root = Tk()
# btn = Button(root, text='click me!', command=inc, font=('', 25))
# btn.place(x=0, y=0, width=200, height=200)
# mainloop()

# Q 3
from tkinter import *
def inc():
    counter = 1
    counter += counter
    if counter < 100:
        btn.config(text=counter)
counter = 1
root = Tk()
btn = Button(root, text='click me!', command=inc, font=('', 25))
btn.place(x=0, y=0, width=200, height=200)
mainloop()
