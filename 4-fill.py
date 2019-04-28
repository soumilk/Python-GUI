from tkinter import *

root= Tk()
root.geometry("350x350")
b1=Button(text="CLick me",fg="blue", bg="yellow")
b1.pack()

b2=Button(text="Hello",fg="red", bg="white")
b2.pack(fill=X)

b3=Button(text="How r u", fg="white",bg="black")
b3.pack(side=RIGHT,fill=Y)

root.mainloop()
