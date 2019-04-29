from tkinter import *

root= Tk()

# Sticky ="E" says to right allign the elements

label1 = Label(root, text="First Name: ")
label1.grid(row=0,column=0,sticky="E")
Entry(root).grid(row=0, column=1)

Label(root,text="Last Name: ").grid(row=1,column=0,sticky="E")
Entry(root).grid(row=1,column=1)

Label(root, text="Password: ").grid(row=2,column=0,sticky="E")
Entry(root).grid(row=2,column=1)

Checkbutton(root,text="Remember Password").grid(row=3,columnspan=2)
