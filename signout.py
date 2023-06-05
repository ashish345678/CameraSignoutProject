from tkinter import*
from tkinter.ttk import*
# from PIL import Image

# Tkinter page
root = Tk()
root.geometry("700x700")
root.title("camera sign out sheet")
label = Label(root, text="Camera Sign Out")
root.configure(bg="beige")
label = Label(root, text="Camera signout")
nikSignout = 3
rebSignout = 3
nikReturn = 0
rebReturn = 0
nikRepair = 0
nikReturn = 0
#im1 = Image.open(r"C:\Users\Vsubramanyam\Downloads\20210511_132009.jpg")

def signoutWindow():
    # Opens the window that is for signing out cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1, width=36)
    text.pack()
    text.place(y=1)
    text.place(x=190, y=10)
    text.insert("1.0", "This page is for signing out cameras")
    cam = Button(newWindow, text = "press to sign out")
    cam.place(x = 280, y = 300)
    cam2 = Button(newWindow, text = "press to sign out"); 

def returnWindow():
    # Opens the window that is for returning cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1, width=34)
    text.pack()
    text.place(y=1)
    text.insert("1.0", "This page is for returning cameras")
def reportWindow():
    # Opens the window that is for reporting damaged cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1, width=42)
    text.pack()
    text.place(y=1)
    text.insert("1.0", "This page is for reporting damaged cameras")
    #reportImage = Image.open("<downloads/camera.JPEG>")


SignOut = Button(root, text="Sign out", command = signoutWindow)
SignOut.place(x = 280, y = 300)

print("Ashish says you need to set a password;")

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