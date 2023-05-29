import tkinter as tk 

root = tk.Tk()

root.geometry("300x300")
root.title("Test")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial',22))
textbox.pack()

root.mainloop()

email = input("What is your gapps email?:")
name = input("What is your full name?:")