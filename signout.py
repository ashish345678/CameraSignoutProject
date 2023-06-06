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
    cam = Button(newWindow, text = "press to sign out")
    cam.place(x = 280, y = 260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", "Nikon", str(nikSignout))
    #nik.place(x = 280, y = 295)
    nik.config(state=DISABLED)
    nik.place(x = 380, y =  260)
    cam2 = Button(newWindow, text = "press to sign out"); 
    cam2.place(x = 280, y = 330)
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", "Rebel", str(rebSignout))
    
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
    nikonReturn = Button(newWindow, text="Return")
    nikonReturn.place(x=335)
    nikonReturn.pack()
    nik = Text(newWindow, height=1, width=7)
    nik.place(x=345)
    nik.insert("1.0", "Nikon", str(nikReturn))
    nik.config(state = DISABLED)
    nik.pack()
    rebelReturn = Button(newWindow, text="Return")
    rebelReturn.place(x=335)
    rebelReturn.pack()
    reb = Text(newWindow, height=1, width=7)
    reb.place(x=345)
    reb.insert("1.0", "Rebel", str(rebReturn))
    reb.config(state = DISABLED)
    reb.pack()
def reportWindow():
    # Opens the window that is for reporting damaged cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    text = Text(newWindow, height=1, width=42)
    text.pack()
    text.place(y=1)
    text.insert("1.0", "This page is for reporting damaged cameras")
    nikonReport = Button(newWindow, text="Report")
    nikonReport.place(x=335)
    nikonReport.pack()
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", "Nikon", str(nikRepair))
    nik.place(x=345)
    nik.config(state = DISABLED)
    nik.pack()
    rebelReport = Button(newWindow, text="Report")
    rebelReport.place(x=335)
    rebelReport.pack()
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", "Rebel", str(rebRepair))
    reb.place(x=345)
    reb.config(state = DISABLED)
    reb.pack()
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