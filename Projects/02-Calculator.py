from tkinter import *

root=Tk()
root.configure(bg="white")
equa=""
equation=StringVar()
calculation=Label(root,textvariable=equation,height=2,font=("Arial",15,"bold"),bg="white")

equation.set("Enter the expression")
calculation.grid(row=0,columnspan=5,pady=2,padx=1)

def equalpress():
       global equa
       total=eval(equa)
       equation.set(total)
       equa=str(total)
       
def pressnum(num):
       global equa
       equa=equa+str(num)
       equation.set(equa)

def erasenum():
       global equa
       equa=equa[:len(equa)-1]
       equation.set(equa)

l=["1","2","3","4","5","6","7","8","9"]
def butt(i,j):
       num=l.pop(0)
       Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text=num
              , relief=RAISED, command=lambda:pressnum(num)).grid(row=i,column=j,padx=2,pady=2)

for i in range(1,4):
       for j in range(1,4):
              butt(i,j)
Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text='+'
              , relief=RAISED, command=lambda:pressnum('+')).grid(row=1,column=4,padx=2,pady=2)
Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text='-'
              , relief=RAISED, command=lambda:pressnum('-')).grid(row=2,column=4,padx=2,pady=2)
Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text='*'
              , relief=RAISED, command=lambda:pressnum('*')).grid(row=3,column=4,padx=2,pady=2)
Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text='/'
              , relief=RAISED, command=lambda:pressnum('/')).grid(row=4,column=4,padx=2,pady=2)
Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text='='
              , relief=RAISED, command=lambda:equalpress()).grid(row=4,column=3,padx=2,pady=2)
Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text='C'
              , relief=RAISED, command=lambda:erasenum()).grid(row=4,column=2,padx=2,pady=2)
Button(root,width=5, height=2, font=("Arial",15,"bold"), fg="#b7005e", bg="#d4f92f", bd=2,text='0'
              , relief=RAISED, command=lambda:pressnum('0')).grid(row=4,column=1,padx=2,pady=2)

root.mainloop()
