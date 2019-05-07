from tkinter import *
import random

root=Tk()
canvas=Canvas(root,width=300,height=300)
canvas.pack()
# creating rectangle and providing the inintial and final x and y coordinates 
canvas.create_rectangle(10,10,200,60)
canvas.create_line(1,2,44,98)
canvas.create_polygon(304,188,69,22,39,86,55,99,fill="lightgreen")

l=["#b7005e","#915574","#5fd3c8","#cfef2f","#db4a11","#a9b5f9",
   "#026d12","#f2fc32","#31fcb1"]
# creating random rectangles
def randomrect(num):
       for i in range (0,num):
              x1=random.randrange(250)
              y1=random.randrange(250)
              x2=x1+random.randrange(100)
              y2=y1+random.randrange(100)
              canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(l))


randomrect(40)
root.mainloop()
