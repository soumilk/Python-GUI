from tkinter import *
from tkinter import messagebox 
root= Tk()
#root.geometry("200x80")

def evaluate(event):
       data=e.get()
       l.configure(text="Answer: "+str(eval(data)))
       
e=Entry(root)
e.pack()
l=Label(root)
l.pack()
e.bind("<Return>",evaluate)

messagebox.showinfo("title","Earth is Round")
ans=messagebox.askquestion("pay attention", "Will you save water")
if ans=="yes":
       messagebox.showinfo("dialogue","You are a good man")
else:
       messagebox.showinfo("Dialogue","You will be dead soon")

root.mainloop()
