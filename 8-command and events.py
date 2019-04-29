from tkinter import *

root= Tk()
root.geometry("500x350")

def leftclick(event):
       print("This is called becasue of event of leftclick")
       
def display():
       print("This is the function call")

def middleclick(event):
       print("This is called because the event of middleclick")

def rightclick(event):
       print("This event is called because the event of right click ")
       
def leftbut(event):
       print("This is the left but")

def rightbut(event):
       print("This is the right but")

Label(root, text="This is the action upon clicking the button through the command on button").grid(row=0,column=0)

b1=Button(root, text="display",command=display,width="18")
b1.grid(row=1,column=0)

Label(root, text="This is the action upon clicking the button through the events").grid(row=3,column=0)
# this will work only when you clik leftclick on button
b2=Button(root,text="through event click1")
b2.bind("<Button-1>",leftclick)
b2.grid(row=4,column=0)

# this will only work when you click middleclick, i.e. scrool button on this
b3=Button(root,text="Through event click2")
b3.bind("<Button-2>",middleclick)
b3.grid(row=5,column=0)

# this will only work when you press right click on this button 
b4=Button(root,text="Through event click3")
b4.bind("<Button-3>",rightclick)
b4.grid(row=6,column=0)

# Bind the left and the right key to the root window
root.bind("<Left>",leftbut)
root.bind("<Right>",rightbut)


root.mainloop()
