from tkinter import *

top = Tk()
top.geometry("300x200")

Label(top, text="Name").place(x=30, y=50)
Label(top, text="Email").place(x=30, y=90)
Label(top, text="Password").place(x=30, y=130)

Entry(top).place(x=100, y=50)
Entry(top).place(x=100, y=90)
Entry(top).place(x=100, y=130)

top.mainloop()
