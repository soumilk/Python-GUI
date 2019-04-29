from tkinter import *

root =Tk()
label=Label(root,text="This is the tkinter window")
# Now after initialising the window, our window wont show any details
# because we have not mentioned it to get attached with the root window.
label.pack()

label2=Label(root,text="This is our second label window")
label2.pack()

butt1= Button(None, text="Just a Button", fg="blue",bg="lightgreen")
butt1.pack()
butt2= Button(None, text="One more", fg="red",bg="yellow")
butt2.pack()
# button with styles of font, color, width, height and border
Button(root,width=10,height=2,font=("Arial",15,"bold"),bd=2,bg="orange",text="hello", fg="green").pack()

# button with relief styles
Button(root,width=10,height=2,font=("Arial",15,"bold"),bd=2,bg="orange",text="Sunken", fg="green",relief=SUNKEN).pack()
Button(root,width=10,height=2,font=("Arial",15,"bold"),bd=2,bg="orange",text="Raised", fg="green",relief=RAISED).pack()
Button(root,width=10,height=2,font=("Arial",15,"bold"),bd=2,bg="orange",text="Ridge", fg="green", relief=RIDGE).pack()
root.mainloop()
