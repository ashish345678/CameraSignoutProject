from tkinter import *
from tkinter.ttk import *

# Tkinter page
root = Tk()
root.geometry("700x700")
root.title("camera sign out sheet")
label = Label(root, text="Camera Sign Out")

# inventory numbers
rebel = 3
nikon = 3

#buttons 
SignOut = Button(root, text="Sign out", height = 5, width = 15)
SignOut.place(x = 280, y = 300)
Return = Button(root, text="return", height = 5, width = 15)
Return.place(x = 100, y = 300)
Report = Button(root, text="report", height = 5, width = 15)
Report.place(x = 450, y = 300)


root.mainloop()

def signout():
    pass
def returncamera():
    pass
def report():
    pass
