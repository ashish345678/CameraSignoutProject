from tkinter import*


root = Tk()
root.geometry("700x700")
root.title("camera sign out sheet")


rebel = 3
nikon = 3
SignOut = Button(root, text="Sign out", height = 5, width = 15)
SignOut.place(x = 280, y = 300)

SignOut = Button(root, text="return", height = 5, width = 15)
SignOut.place(x = 100, y = 300)

SignOut = Button(root, text="report", height = 5, width = 15)
SignOut.place(x = 450, y = 300)


root.mainloop()
