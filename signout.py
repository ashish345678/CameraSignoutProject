from tkinter import*
from tkinter.ttk import*

# Tkinter page
root = Tk()
root.geometry("700x700")
root.title("camera sign out sheet")
label = Label(root, text="Camera Sign Out")
root.configure(bg="beige")

def signoutWindow():
    # Opens the window that is for signing out cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1)
    text.pack()
    text.place(y=600)
    text.insert("1.0", "This page is for signing out cameras")

def returnWindow():
    # Opens the window that is for returning cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1)
    text.pack()
    text.place(y=600)
    text.insert("1.0", "This page is for returning cameras")

def reportWindow():
    # Opens the window that is for reporting damaged cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1)
    text.pack()
    text.place(y=600)
    text.insert("1.0", "This page is for reporting damaged cameras")

rebel = 3
nikon = 3
SignOut = Button(root, text="Sign out", command=signoutWindow)
SignOut.place(x = 280, y = 300)


Return = Button(root, text="return", command=returnWindow)
Return.place(x = 100, y = 300)

Report = Button(root, text="report", command=reportWindow)
Report.place(x = 450, y = 300)


root.mainloop()

def signout():
    pass
def returncamera():
    pass

def report():
    pass