from tkinter import*
from tkinter.ttk import*
import random
import csv
import os
import tkinter.messagebox
from PIL import ImageTk, Image

folder = os.getcwd()

# Tkinter page
root = Tk()
root.geometry("2000x1000")
root.title("camera sign out sheet")
label = Label(root, text="Camera Sign Out", font = ('ariel', 22))
label.place(height=75, width=235)
label.place(x = 650, y=150)
root.configure(bg="beige")
with open('camerastock.csv') as file:
    open = file.read()
    line = open.split()
    
print(line)
nikSignout = int(line[3][6])
rebSignout = int(line[6][6])
nikReturn =  int(line[9][4])
rebReturn =  int(line[12][4])
nikRepair =  int(line[15][7])
rebRepair =  int(line[18][7])
img1 = ImageTk.PhotoImage(Image.open(folder + "\\camera.JPEG"))
panel = Label(root, image = img1)
panel.pack(side="bottom", fill="both", expand="yes")


def signoutWindow():
    # Opens the window that is for signing out cameras
    newWindow = Toplevel(root)          # Creates the window and sets it on the top level
    newWindow.geometry("2000x1000")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")     # Changes the background of the window
    text = Text(newWindow, height=1, width=36)
    text.pack()
    text.place(x=600, y=30)
    text.insert("1.0", "This page is for signing out cameras")
    text.config(state=DISABLED)
    #window that opens when nikon is chosen
    def nikEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("2000x1000")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global nikReturn
            global nikSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if nikSignout == 0:
                    tkinter.messagebox.showinfo("Ran Out", "We have run out of Nikons")
                else:
                    nikSignout = nikSignout -1
                    nikReturn = nikReturn + 1
                    tkinter.messagebox.showinfo("Received", "Your camera has been signed out, Thank you.")
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.")
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED)
        emailText.pack()
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail())
        getEmail.pack()
        
    cam = Button(newWindow, text = "press to sign out", command = lambda: nikEmailWindow())
    cam.place(x = 630, y = 260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikSignout))
    nik.config(state=DISABLED)
    nik.place(x = 730, y =  260)
    #Window that opens when rebel is chosen
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("2000x1000")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global rebReturn
            global rebSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if rebSignout == 0:
                    tkinter.messagebox.showinfo("Ran Out", "We have run out of Rebels")
                else:
                    rebSignout = rebSignout - 1
                    rebReturn =  rebReturn + 1
                    tkinter.messagebox.showinfo("Received", "Your camera has been signed out, Thank you.")
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.")
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED)
        emailText.pack()
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail())
        getEmail.pack()
        
    cam2 = Button(newWindow, text = "press to sign out", command = lambda:rebEmailWindow())
    cam2.place(x = 630, y = 330)
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", ("Rebel", rebSignout))
    reb.config(state = DISABLED)
    reb.place(x= 730, y = 330)


def returnWindow():
    # Opens the window that is for returning cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("2000x1000")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    #title page 
    text = Text(newWindow, height=1, width=36)
    text.pack()
    text.place(x=600, y=30)
    text.insert("1.0", "This page is for returning cameras")
    text.config(state=DISABLED)
    def nikEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("2000x1000")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global nikReturn
            global nikSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if nikReturn == 0:
                    tkinter.messagebox.showinfo("Ran Out", "We have run out of Nikons")
                else:
                    nikReturn = nikReturn - 1
                    nikSignout = nikSignout + 1
                    tkinter.messagebox.showinfo("Received", "Your camera has been returned, Thank you.")
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.")
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED)
        emailText.pack()
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail())
        getEmail.pack()
    #to return a nikon
    nikonReturn = Button(newWindow, text="Return", command=lambda: nikEmailWindow())
    nikonReturn.place(x=630, y=260)
    nik = Text(newWindow, height=1, width=7)
    nik.place(x = 715, y = 260)
    nik.insert("1.0", ("Nikon", nikReturn))
    nik.config(state = DISABLED)
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("2000x1000")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global rebReturn
            global rebSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if rebReturn == 0:
                    tkinter.messagebox.showinfo("Ran Out", "We have run out of Rebels")
                else:
                    rebReturn = rebReturn - 1
                    rebSignout = rebSignout + 1
                    tkinter.messagebox.showinfo("Received", "Your camera has been returned, Thank you.")
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.")
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED)
        emailText.pack()
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail())
        getEmail.pack()
    #button to return a rebel
    rebelReturn = Button(newWindow, text="Return", command=lambda: rebEmailWindow())
    rebelReturn.place(x= 630, y = 330)
    reb = Text(newWindow, height=1, width=7)
    reb.place(x= 715, y = 330)
    reb.insert("1.0", ("Rebel", rebReturn))
    reb.config(state = DISABLED)


def reportWindow():
    # Opens the window that is for reporting damaged cameras
    newWindow = Toplevel(root)          
    newWindow.geometry("2000x1000")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")
    #title page
    text = Text(newWindow, height=1, width=42)
    text.pack()
    text.place(x=600, y=30)
    text.insert("1.0", "This page is for reporting damaged cameras")
    text.config(state=DISABLED)
    def nikEmailWindow():
        # A window for collecting the information of the user reporting a camera
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("2000x1000")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global nikReturn
            global nikReport
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if nikReturn == 0:
                    tkinter.messagebox.showinfo("No cameras", "There are no cameras that can be reported")
                else:
                    nikReturn = nikReturn - 1
                    nikReport = nikReport +1
                    
                    tkinter.messagebox.showinfo("Received", "We'll take a look at this, Thank you.")
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.")
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED)
        emailText.pack()
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail())
        getEmail.pack()
        
    #Button to report a nikon
    nikonReport = Button(newWindow, text="Report", command=lambda: nikEmailWindow())
    nikonReport.place(x=700, y=260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikRepair))
    nik.place(x=780, y=260)
    nik.config(state = DISABLED)

    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("2000x1000")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global rebReturn
            global rebReport
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if rebSignout == 0:
                    tkinter.messagebox.showinfo("No cameras", "There are no cameras that can be reported")
                else:
                    rebReport = rebReport + 1
                    rebReturn =  rebReturn - 1
                    tkinter.messagebox.showinfo("Received", "We'll take a look at this, Thank you.")
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.")
    
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED)
        emailText.pack()
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail())
        getEmail.pack()

    #button to report a rebel 
    rebelReport = Button(newWindow, text="Report", command=lambda: rebEmailWindow())
    rebelReport.place(x= 700, y = 330)
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", ("Rebel",rebRepair))
    reb.place(x= 780, y = 330)
    reb.config(state = DISABLED)
    #reportImage = Image.open("<downloads/camera.JPEG>")


SignOut = Button(root, text="Sign out", command = signoutWindow)
SignOut.place(x = 700, y = 300)
SignOut.place(height=75, width=125)

Return = Button(root, text="return", command=returnWindow)
Return.place(x = 280, y = 300)
Return.place(height=75, width=125)

Report = Button(root, text="Report", command=reportWindow)
Report.place(x = 1100, y = 300)
Report.place(height=75, width=125)



root.mainloop()

def signout():
    pass
def returncamera():
    pass

def report():
    pass
file.close()