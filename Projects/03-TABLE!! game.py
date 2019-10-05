
from tkinter import *
root=Tk()
root.title("The table game")
#root.geometry("1150x700")
root["bg"]="#fff79a"
root.state('zoomed')
background_image=PhotoImage(file="math2.png")
background_label = Label(image=background_image)
background_label.grid(row=0,column=0,columnspan=25,rowspan=30)
def f(x):
       Button(root,width=5,height=2,font=("Arial",9,"bold"),bd=1,bg="yellow",text=x[0]*x[1], fg="red").grid(
                     row=x[0],column=x[1],padx=2,pady=2)
for i in range(1,16):
       Label(root,text=str(i),width=5, height=2, font=("Arial",10,"bold"),bd=2,
             bg="#61f46b", fg="red").grid(row=0, column=i, padx=5, pady=5)

for i in range(1,16):
       Label(root,text=str(i),width=5, height=2,font=("Arial",10,"bold"),bg="#61f46b",fg="red").grid(
              row=i,column=0,padx=2, pady=2)
for i in range(1,16):
       for j in range(1,16):
              Button(root,width=5,height=2,bg="powderblue",command=lambda x=(i,j):f(x), fg="red").grid(
                     row=i,column=j,padx=2,pady=2)
root.mainloop()
