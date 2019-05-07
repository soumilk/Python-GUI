from tkinter import *
import random
from tkinter import messagebox
import time

root=Tk()
root.title("Pong Game")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas=Canvas(root,width=600, height=500, bd=1,highlightthickness=1)
canvas.config(bg="black")
canvas.pack()
l=canvas.create_text(300,20,font=("Arial",20,"bold"),text=" : ",fill="white")

root.update()
canvas.create_line(300,0,300,600,fill="white")

class Ball:
       def update(self):
              l.configure(text=str(self.score1)+' : '+str(self.score2))
       
       def __init__(self,canvas,paddle1,paddle2,color):
              self.paddle1=paddle1
              self.paddle2=paddle2
              self.canvas=canvas
              self.id=canvas.create_oval(10,10,30,30,fill=color)
              self.canvas.move(self.id,283,300)
              starts=[-3,-2,-1,1,2,3]
              random.shuffle(starts)
              self.x=starts[1]
              self.y=starts[2]
              self.canvas_height=self.canvas.winfo_height()
              self.canvas_width =self.canvas.winfo_width()
              self.score1=0
              self.score2=0
              
              
       def draw(self):
              self.canvas.move(self.id,self.x,self.y)
              pos=self.canvas.coords(self.id)
              if pos[1]<=0:
                     self.y=4
              if pos[3]>=self.canvas_height:
                     self.y=-4
              if pos[0]<=0:
                     self.x=4
                     self.score1+=1
                     print(self.score1)
                     canvas.itemconfigure(l,text=str(self.score1)+" : "+str(self.score2))
                     #update()
              if pos[2]>=self.canvas_width:
                     self.x=-4
                     self.score2+=1
                     print(self.score2)
                     canvas.itemconfigure(l,text=str(self.score1)+" : "+str(self.score2))
                     #update()
              if self.hit_paddle1(pos)==True:
                     self.x=4
              if self.hit_paddle2(pos)==True:
                     self.x=-4

       def hit_paddle1(self,pos):
              paddle_pos=self.canvas.coords(self.paddle1.id)
              if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
                     if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                            return True
                     return False

       def hit_paddle2(self,pos):
              paddle_pos=self.canvas.coords(self.paddle2.id)
              if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
                     if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                            return True
                     return False
              

class Paddle1:
       pos=[0,0,0,0]
       def __init__(self,canvas,color):
              self.canvas=canvas
              self.id=canvas.create_rectangle(10,180,25,280,fill=color)
              self.y=0
              self.canvas_height=self.canvas.winfo_height()
              self.canvas_width=self.canvas.winfo_width()
              self.canvas.bind_all('a',self.turn_left)
              self.canvas.bind_all('d',self.turn_right)
       def draw(self):
              self.canvas.move(self.id,0,self.y)
              pos=self.canvas.coords(self.id)
              if pos[1]<=0:
                     self.y=0
              if pos[3]>=self.canvas_height:
                     self.y=0
              
       def turn_left(self,event):
              self.y=-4
       def turn_right(self,event): 
              self.y=4

class Paddle2:
       pos=[0,0,0,0]
       def __init__(self,canvas,color):
              self.canvas=canvas
              self.id=canvas.create_rectangle(575,180,590,280,fill=color)
              self.y=0
              self.canvas_height=self.canvas.winfo_height()
              self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
              self.canvas.bind_all("<KeyPress-Right>",self.turn_right)

       def draw(self):
              self.canvas.move(self.id,0,self.y)
              pos=self.canvas.coords(self.id)
              if pos[1]<=0:
                     self.y=0
              if pos[3]>=self.canvas_height:
                     self.y=0

       def turn_left(self,event):
              self.y=4
       def turn_right(self,event): 
              self.y=-4
                     
              
middle_circle=canvas.create_oval(10,10,150,150,outline="white")
canvas.move(middle_circle,220,170)

paddle1=Paddle1(canvas,"orange")
paddle2=Paddle2(canvas,"lightgreen")
ball=Ball(canvas,paddle1,paddle2,"yellow")

while 1:
       if ball.score1==10 or ball.score2==10:
              messagebox.showinfo("Game Over","Player 1 ="+str(ball.score1)+" Player 2 ="+str(ball.score2))
              break
       ball.draw()
       paddle1.draw()
       paddle2.draw()
       root.update_idletasks()
       root.update()
       time.sleep(0.01)
       
root.mainloop()
