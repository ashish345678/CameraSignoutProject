from tkinter import*
from tkinter.ttk import*
# from PIL import Image

# Tkinter page
root = Tk()
root.geometry("700x700")
root.title("camera sign out sheet")
label = Label(root, text="Camera Sign Out", font = ('ariel', 22))
root.configure(bg="beige")
label.place(x = 220 , y=40)
nikSignout = 3
rebSignout = 3
nikReturn = 0
rebReturn = 0
nikRepair = 0
rebRepair = 0
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
    text.config(state=DISABLED)
    cam = Button(newWindow, text = "press to sign out") # When clicked creates a new window 
    cam.place(x = 280, y = 260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikSignout))
    #nik.place(x = 280, y = 295)
    nik.config(state=DISABLED)
    nik.place(x = 380, y =  260)
    cam2 = Button(newWindow, text = "press to sign out") # When clicked creates a new window 
    cam2.place(x = 280, y = 330)
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", ("Rebel", rebSignout))

    reb.config(state = DISABLED)
    reb.place(x= 380, y = 330)


def returnWindow():
    # Opens the window that is for returning cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1, width=36)
    text.pack()
    text.place(y=1)
    text.place(x=190, y=10)
    text.insert("1.0", "This page is for returning cameras")
    text.config(state=DISABLED) 
    nikonReturn = Button(newWindow, text="Return") # When clicked creates a new window 
    nikonReturn.place(x=280, y=260)
    nik = Text(newWindow, height=1, width=7)
    nik.place(x=360, y=260)
    nik.insert("1.0", ("Nikon", nikReturn))
    nik.config(state = DISABLED)
    rebelReturn = Button(newWindow, text="Return") # When clicked creates a new window 
    rebelReturn.place(x=280, y=330)
    reb = Text(newWindow, height=1, width=7)
    reb.place(x=360, y=330)
    reb.insert("1.0", ("Rebel", rebReturn))
    reb.config(state = DISABLED)
def reportWindow():
    # Opens the window that is for reporting damaged cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1, width=42)
    text.pack()
    text.place(x=190, y=10)
    text.insert("1.0", "This page is for reporting damaged cameras")
    text.config(state=DISABLED)
    nikonReport = Button(newWindow, text="Report") # When clicked creates a new window 
    nikonReport.place(x=280, y=260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikRepair))
    nik.place(x=360, y=260)
    nik.config(state = DISABLED)
    rebelReport = Button(newWindow, text="Report") # When clicked creates a new window 
    rebelReport.place(x=280, y=330)
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", ("Rebel",rebRepair))
    reb.place(x=360, y=330)
    reb.config(state = DISABLED)
    #reportImage = Image.open("<downloads/camera.JPEG>")


SignOut = Button(root, text="Sign out", command = signoutWindow)
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