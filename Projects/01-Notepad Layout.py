from tkinter import *
from tkinter import Menu
root=Tk()
root.title("Notepad")
#root.geometry('890x550')
def f():
       print("Hello")

t=Text(root)
t.pack(fill=BOTH)
menubar=Menu(root)
root.state('zoomed')

# creating the file pull down
filemenu=Menu(menubar)
l=["New","Option","Save","Save as","Page layout","Exit"]
for i in l:
       filemenu.add_command(label=str(i), command=f)
menubar.add_cascade(label="File",menu=filemenu)

# creating the Edit pull down
filemenu=Menu(menubar)
l=["Undo","Cut","Copy","Paste","Find","Delete","Find","Replace","Goto","Selectall"]
for i in l:
       filemenu.add_command(label=str(i), command=f)
menubar.add_cascade(label="Edit",menu=filemenu)

# creating the Format pull down
filemenu=Menu(menubar)
l=["Word Wrap","Font"]
for i in l:
       filemenu.add_command(label=str(i), command=f)
menubar.add_cascade(label="Format",menu=filemenu)

# creating the View pull down
filemenu=Menu(menubar)
l=["Status bar"]
for i in l:
       filemenu.add_command(label=str(i), command=f)
menubar.add_cascade(label="View",menu=filemenu)

# creating the Help pull down
filemenu=Menu(menubar)
l=["View help","About notepad"]
for i in l:
       filemenu.add_command(label=str(i), command=f)
menubar.add_cascade(label="Help",menu=filemenu)
menubar.add_command(label="Quit", command=root.destroy)

pop=Menu(root)
l1=["Undo","Cut","Copy","Select all","Right to left reading order","Delete"]
for i in l1: 
       pop.add_command(label=str(i),command=f)

frame=Frame(root,width=512,height=512)
frame.pack()

def popup(event):
       pop.post(event.x_root,event.y_root)
       
frame.bind("<Button-3>",popup)

root.config(menu=menubar)
root.mainloop()
