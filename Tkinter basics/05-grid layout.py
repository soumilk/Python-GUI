from tkinter import *

root= Tk()
root.geometry("350x350")

b1=Button(text="CLick me",fg="blue", bg="yellow")
b1.grid(row=0,column=0)

b2=Button(text="Hello",fg="red", bg="white")
b2.grid(row=3,column=4)

b3=Button(text="How r u", fg="white",bg="black")
b3.grid(row=2,column=2)
root.mainloop()

