from tkinter import*
from tkinter.ttk import*
import random
import csv
import os
# from PIL import Image

# Tkinter page
root = Tk()
root.geometry("700x700")
root.title("camera sign out sheet")
label = Label(root, text="Camera Sign Out", font = ('ariel', 22))
root.configure(bg="beige")
label.place(x = 220 , y=40)
with open('camerastock.csv') as file:
    open = file.read()
    line = open.split()
    
print(line)
nikSignout = int(line[3][6])
rebSignout = int(line[6][6])
nikReturn =  int(line[9][4])
rebReturn =  int(line[12][4])
nikRepair =  int(line[15][7])
rebRepair = int(line[18][7])
#im1 = Image.open(r"C:\Users\Vsubramanyam\Downloads\20210511_132009.jpg")


def signoutWindow():
    # Opens the window that is for signing out cameras
    newWindow = Toplevel(root)          # Creates the window and sets it on the top level
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")     # Changes the background of the window
    text = Text(newWindow, height=1, width=36)
    text.pack()
    text.place(y=1)
    text.place(x=190, y=10)
    text.insert("1.0", "This page is for signing out cameras")
    text.config(state=DISABLED)
    #window that opens when nikon is chosen
    def nikEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        global nikSignout 
        global nikReturn
        if nikSignout == 0:
            nope = Label(newEmailWindow, text = "rebel ran out")
            nope.place()
        else:
            nikSignout = nikSignout - 1
            nikReturn = nikReturn + 1
        
    cam = Button(newWindow, text = "press to sign out", command = lambda: nikEmailWindow())
    cam.place(x = 280, y = 260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikSignout))
    nik.config(state=DISABLED)
    nik.place(x = 380, y =  260)
    #Window that opens when rebel is chosen
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        global rebSignout
        global rebReturn
        if rebSignout == 0:
            nope = Label(newEmailWindow, text = "rebel ran out")
        else:
            rebSignout = rebSignout - 1
            rebReturn = rebReturn + 1
        
    cam2 = Button(newWindow, text = "press to sign out", command = lambda:rebEmailWindow())
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
    #title page 
    text = Text(newWindow, height=1, width=36)
    text.pack()
    text.place(y=1)
    text.place(x=190, y=10)
    text.insert("1.0", "This page is for returning cameras")
    text.config(state=DISABLED)
    def nikEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        global nikReturn
        global nikSignout
        if nikReturn == 0:
            nope = Label(newEmailWindow, text = "rebel ran out")
        else:
            nikReturn = nikReturn - 1
            nikSignout = nikSignout + 1
    #to return a nikon
    nikonReturn = Button(newWindow, text="Return", command=lambda: nikEmailWindow())
    nikonReturn.place(x=280, y=260)
    nik = Text(newWindow, height=1, width=7)
    nik.place(x=360, y=260)
    nik.insert("1.0", ("Nikon", nikReturn))
    nik.config(state = DISABLED)
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        global rebReturn
        global rebSignout
        if rebReturn == 0:
            nope = Label(newEmailWindow, text = "rebel ran out")
        else:
            rebReturn = rebReturn - 1
            rebSignout = rebSignout + 1
    #button to return a rebel
    rebelReturn = Button(newWindow, text="Return", command=lambda: rebEmailWindow())
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
    #title page
    text = Text(newWindow, height=1, width=42)
    text.pack()
    text.place(x=190, y=10)
    text.insert("1.0", "This page is for reporting damaged cameras")
    text.config(state=DISABLED)
    def nikEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")
        emailText.place(x=190, y=10)
        emailText.config(state=DISABLED)
        emailText.pack()
    #Button to report a nikon
    nikonReport = Button(newWindow, text="Report", command=lambda: nikEmailWindow())
    nikonReport.place(x=280, y=260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikRepair))
    nik.place(x=360, y=260)
    nik.config(state = DISABLED)
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
    #button to report a rebel
    rebelReport = Button(newWindow, text="Report", command=lambda: rebEmailWindow())
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
file.close()