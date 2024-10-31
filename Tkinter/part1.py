# Widgets = GUI elements like buttons, labels, textboxes,images etc.
# Windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk()                 #instantiates an instance of a window

window.geometry("420x420")    #sets the window size

window.title("My First GUI")  #sets the window title



window.mainloop()             #places the window on the screen, and listens for events