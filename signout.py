from tkinter import*
from tkinter.ttk import*
import random
import csv
import os
import tkinter.messagebox
#from PIL import ImageTk, Image

folder = os.getcwd()

# Tkinter page
root = Tk()
root.geometry("700x700")
root.title("camera sign out sheet")
label = Label(root, text="Camera Sign Out", font = ('ariel', 22))
label.place(x = 220, y=40)
root.configure(bg="beige")
with open('camerastock.csv') as file:
    open = file.read()
    line = open.split()
    
print(line)
# # of cams in each category 
nikSignout = int(line[3][6])
rebSignout = int(line[6][6])
nikReturn =  int(line[9][4])
rebReturn =  int(line[12][4])
nikReport=  int(line[15][7])
rebReport=  int(line[18][7])
AdminPass = "youwannagetnutsletsgetnuts" 
#img1 = ImageTk.PhotoImage(Image.open(folder + "\\camera.JPEG"))
#panel = Label(root, image = img1)
#panel.place(x=600, y=450)


def signoutWindow():
    # Opens the window that is for signing out cameras
    newWindow = Toplevel(root)          # Creates the window and sets it on the top level
    newWindow.geometry("700x700")       # Sets the geometry of the new window
    newWindow.configure(bg="beige")     # Changes the background of the window
    text = Text(newWindow, height=1, width=36)
    text.pack()
    text.place(x=190, y=10)       # changes the location of where the text is on the page
    text.insert("1.0", "This page is for signing out cameras") # tittle for the page 
    text.config(state=DISABLED)  # Text cannot be edited 
    #window that opens when nikon is chosen
    def nikEmailWindow():
        newEmailWindow = Toplevel(newWindow) # Creates the window and sets it on the top level
        newEmailWindow.geometry("700x700") # Sets the geometry of the new window
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global nikReturn
            global nikSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   # makes it where if the email doesn't have ".", "@" and "gapps"
                if nikSignout == 0:
                    tkinter.messagebox.showinfo("Ran Out", "We have run out of Nikons")     # if there are no more nikons left prints this messagebox 
                else:
                    nikSignout = nikSignout -1      # minus one from signout when email is valid 
                    nikReturn = nikReturn + 1       # Adds one from return when email is valid 
                    tkinter.messagebox.showinfo("Received", "Your camera has been signed out, Thank you.") #prints message if valid 
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.") # prints if user types wrong email 
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?")  # prints tittle 
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED)  #not able to edit text
        emailText.pack() 
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail()) # press to enter email
        getEmail.pack()
        
    cam = Button(newWindow, text = "press to sign out", command = lambda: nikEmailWindow()) #press to sign out nikon 
    cam.place(x = 280, y = 260)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikSignout)) # Adds Nikon to the text 
    nik.config(state=DISABLED)
    nik.place(x = 380, y = 260)
    #Window that opens when rebel is chosen
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow) # Creates the window and sets it on the top level
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global rebReturn
            global rebSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:    # makes it where if the email doesn't have ".", "@" and "gapps"
                if rebSignout == 0:
                    tkinter.messagebox.showinfo("Ran Out", "We have run out of Rebels") # if there are no more nikons left prints this messagebox 
                else:
                    rebSignout = rebSignout - 1 # minus one from signout when email is valid 
                    rebReturn =  rebReturn + 1   # Adds one from return when email is vali
                    tkinter.messagebox.showinfo("Received", "Your camera has been signed out, Thank you.")  #prints message if valid 
            else:
                tkinter.messagebox.showinfo("Incorrect Email", "Your email is invalid, please try again.") # prints if user types wrong email
        emailText = Text(newEmailWindow, height=1, width=19)
        emailText.insert("1.0", "What is your email?") # prints tittle 
        emailText.place(x=190, y=70)
        emailText.config(state=DISABLED) #not able to edit text
        emailText.pack()
        emailInput = Entry(newEmailWindow)
        emailInput.pack()
        getEmail = Button(newEmailWindow, text="Enter", command=lambda: collectEmail()) # press to enter email
        getEmail.pack()
        
    cam2 = Button(newWindow, text = "press to sign out", command = lambda:rebEmailWindow()) #press to sign out rebel 
    cam2.place(x = 280, y = 330)
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", ("Rebel", rebSignout)) # Adds Nikon to the text 
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
    text.place(x=190, y=10)
    text.insert("1.0", "This page is for returning cameras")
    text.config(state=DISABLED)
    def nikEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global nikReturn
            global nikSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if nikReturn == 0:
                    tkinter.messagebox.showinfo("Ran Out", "No Nikions can be returned ")
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
    nikonReturn.place(x=280, y=260)
    nik = Text(newWindow, height=1, width=7)
    nik.place(x = 360, y = 260)
    nik.insert("1.0", ("Nikon", nikReturn))
    nik.config(state = DISABLED)
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global rebReturn
            global rebSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if rebReturn == 0:
                    tkinter.messagebox.showinfo("Ran Out", "No Rebels can be returned")
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
    rebelReturn.place(x= 280, y = 330)
    reb = Text(newWindow, height=1, width=7)
    reb.place(x= 360, y = 330)
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
        # A window for collecting the information of the user reporting a camera
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global nikReport
            global nikSignout
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if nikSignout == 0:
                    tkinter.messagebox.showinfo("No cameras", "There are no cameras that can be reported.")
                else:
                    nikSignout = nikSignout - 1
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
    nikonReport.place(x=280, y=330)
    nik = Text(newWindow, height=1, width=7)
    nik.insert("1.0", ("Nikon", nikReport))
    nik.place(x=360, y=330)
    nik.config(state = DISABLED)
    def rebEmailWindow():
        newEmailWindow = Toplevel(newWindow)
        newEmailWindow.geometry("700x700")
        newEmailWindow.configure(bg="beige")
        def collectEmail():
            global rebSignout
            global rebReport
            emailValue = emailInput.get()
            if "." in emailValue and "@" in emailValue and "gapps" in emailValue:   
                if rebSignout == 0:
                    tkinter.messagebox.showinfo("No cameras", "There are no cameras that can be reported.")
                else:
                    rebReport = rebReport + 1
                    rebSignout = rebSignout - 1
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
    rebelReport.place(x= 280, y = 260)
    reb = Text(newWindow, height=1, width=7)
    reb.insert("1.0", ("Rebel",rebReport))
    reb.place(x= 360, y = 260)
    reb.config(state = DISABLED)
    
    def RestoreReb():
        pass

    def RestoreNik():
        newRestoreWindow = Toplevel(newWindow)
        newRestoreWindow.geometry("700x700")
        newRestoreWindow.configure(bg="beige")

        def collectPassword():
            global AdminPass
            global nikReport
            global nikSignout
            passwordValue = passwordInput.get()
            if passwordValue == AdminPass:
                if nikReport == 0:
                    tkinter.messagebox.showinfo("No Damage", "There are no cameras that are in for repairs.")
                else:
                    nikSignout = nikSignout + 1
                    nikReport = nikReport - 1
                    tkinter.messagebox.showinfo("Received", "The camera has been put up for signout.")
            else:
                tkinter.messagebox.showinfo("Incorrect", "The password you used was incorrect, please try again.")

        passwordText = Text(newRestoreWindow, height=1, width=20)
        passwordText.insert("1.0", "What's the password?")
        passwordText.place(x=190, y=70)
        passwordText.config(state=DISABLED)
        passwordText.pack()
        passwordInput = Entry(newRestoreWindow)
        passwordInput.pack()
        getPassword = Button(newRestoreWindow, text="enter", command=lambda: collectPassword())
        getPassword.pack()

    nikRestore = Button(newWindow, text="Restore Nikon", command=lambda: RestoreNik())
    nikRestore.place(x=300, y=430)
    #reportImage = Image.open("<downloads/camera.JPEG>")


SignOut = Button(root, text="Sign out", command = signoutWindow)
SignOut.place(x = 280, y = 300)
SignOut.place(height=75, width=125)


Return = Button(root, text="return", command=returnWindow)
Return.place(x = 100, y = 300)
Return.place(height=75, width=125)


Report = Button(root, text="Report", command=reportWindow)
Report.place(x = 450, y = 300)
Report.place(height=75, width=125)



root.mainloop()

def signout():
    pass
def returncamera():
    pass

def report():
    pass
file.close()