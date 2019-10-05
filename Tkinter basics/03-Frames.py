from tkinter import *

root= Tk()

topframe=Frame(root, bg="pink")
topframe.pack()
root.geometry("480x480")
botframe=Frame(root,bg="yellow")
botframe.pack(side=BOTTOM)

button1=Button(topframe,text="hello")
button1.pack(side=LEFT)
button2=Button(topframe,text="hello")
button2.pack(side=LEFT)
button5=Button(topframe,text="hello, how are you")
button5.pack(side=LEFT)

button3=Button(botframe,text="Bello")
button3.pack(side=LEFT)
button4=Button(botframe,text="hello")
button4.pack(side=LEFT)

