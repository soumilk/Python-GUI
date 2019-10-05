from tkinter import *

root= Tk()
root.geometry("350x350")
# Here you can see that the width of 1 grid cell adjusts according to the widgets

b1=Button(text="CLick me",fg="blue", bg="yellow")
b1.grid(row=0,column=0)

b2=Button(text="Hello",fg="red", bg="white")
b2.grid(row=3,column=4)

b3=Button(text="How r u", fg="white",bg="black")
b3.grid(row=2,column=2)

e1=Entry(root)
e1.grid(row=1,column=1)

e2=Entry(root)
e2.grid(row=3,column=0)

label1=Label(root,text="Name:")
label1.grid(row=4,column=0)

e1=Entry(root)
e1.grid(row=4,column=1)

ch=Checkbutton(root,text="Remember me!")
ch.grid(row=5,columnspan=2)


root.mainloop()

