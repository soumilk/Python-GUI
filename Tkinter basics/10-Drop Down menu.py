from tkinter import *

root=Tk()

def func():
       print("This is the function")
       
mainmenu=Menu(root)
root.configure(menu=mainmenu)

sub1=Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=sub1)   #for dropdown
sub1.add_cascade(label="Random command",command=func)
sub1.add_cascade(label="Format",command=func)

sub1.add_separator()
sub1.add_cascade(label="find",command=func)

sub2=Menu(mainmenu)
mainmenu.add_cascade(label="Edit",menu=sub2)
sub2.add_cascade(label="font")
sub2.add_cascade(label="Stylish color")

root.mainloop()
