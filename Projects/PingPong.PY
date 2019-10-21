import pygame
import random
import os


pygame.init() #initiialize pygame
screen = pygame.display.set_mode((800, 600),pygame.DOUBLEBUF) # setup screen
done=False
is_blue = True
# dimensions of table
x_table, y_table, w_table, h_table=(0, 0, 800, 600)

# dimension pf player slate
initial_position_player=(350,560,100,40)

# dimension pf cpu slate
initial_position_cpu=(350,0,100,40)
#center of Table
center_table=(int(x_table+(w_table/2)),int(y_table+(h_table/2)))


Stride=6  #stride of plate  
clock = pygame.time.Clock()


# Paddle class
class Paddle():
    """
    screen: Main surface or screen on which it is drawn
    initial pos:initial postion of paddle. Tuple of(x,y.width,hight)
    Stride: Distance moved per key press
    """
    def __init__(self,screen,initial_pos,Stride):
        self.x=initial_pos[0]
        self.y=initial_pos[1]
        self.w=initial_pos[2]
        self.h=initial_pos[3]
        self.screen=screen
        self.draw()
        self.Stride=Stride
        self.score=0

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(self.x,self.y,self.w,self.h))
    
    def position(self): #Return Position
        return (self.x,self.y,self.w,self.h)

    def move_left(self): # move left
        width,_= self.screen.get_size()
        if self.x>=0:
            self.x-=self.Stride
        self.draw()
    
    def move_right(self): # move Right 
        width,_= self.screen.get_size()
        if self.x<=width-self.w:
            self.x+= self.Stride
        self.draw()


### Ball -Class
class Ball():
    def __init__(self,screen,center,speed,player,cpu):
        self.radius=10

        self.center=center
        self.screen=screen
        self.speed_x=speed[0]
        self.speed_y=speed[1]

        self.x1=center[0]-self.radius
        self.x2=center[0]+self.radius
        self.y1=center[1]-self.radius
        self.y2=center[1]+self.radius
        self.p1=player
        self.p2=cpu
        self.collide_count=0
        self.draw()
        self.move()

    
        
    #return Ball position:
    def get_ball_postions(self):
        return(self.center,self.x1,self.x2,self.y1,self.y2)
    
    def draw(self):
        #print( self.center)
        pygame.draw.circle(self.screen,(255,0,0),self.center,self.radius)
    
    def move(self):
        width,hieght=self.screen.get_size() # width and hieght of the scene
        
        #self.center,self.x1,self.x2,self.y1,self.y2=self.get_ball_postions()
        self.center = (self.center[0]+self.speed_x,self.center[1]+self.speed_y)
        self.x1=max(self.x1+self.speed_x,0)
        self.x2=min(self.x2+self.speed_x,width)
        self.y1=max(self.y1+self.speed_y,0)
        self.y2=min(self.y2+self.speed_y,hieght)
        
        # stops the ball if boundary hits the ball
        if self.hit_boundary():

            if self.which_boundary()=="x": 
                self.speed_x= (-1)*int(self.speed_x)# reverse xdirection
            
            if self.which_boundary()=="y":
                 self.speed_y= (-1)*int(self.speed_y) # reverse y direction
                
        # INCREASE THE SCORE
        if self.player_collision() :
            self.p1.score=self.p1.score+1
            self.speed_y = (-1)*int(self.speed_y)
        
        if self.cpu_collision():
            self.p2.score=self.p2.score+1
            self.speed_y = (-1)*int(self.speed_y)
        
        
        # INCREASES THE SPEED WHENEVEVR the SCORE OF PLAYER INCREASES BY 5
        if self.p1.score % 10 or self.p2.score % 10 :
                self.speed_y = (-1)*int(self.speed_y+ 1)
                #self.speed_x = int(self.speed_x+ 1)


        self.draw()

    # condition to check if ball is out of playground
    def ball_on_table(self):   
        width,hieght=self.screen.get_size()
        if self.center[0]>=0 and self.center[1]>=0 and self.center[0]<width+self.radius and self.center[1]<hieght+self.radius:
            return True
    
    # checks condition for boundary hit 
    def hit_boundary(self):
        width,hieght=self.screen.get_size()
        if self.x1==0 or self.x2==width or self.y1==0 or self.y2==hieght  :
            return True
    
    # checks which boundary ball collides
    def which_boundary(self):
        width,hieght=self.screen.get_size()
        if self.x1==0 or self.x2==width :
            return "x"
        if self.y1==0 or self.y2==hieght:
            return "y"

    # checks If  ball collides with player paddle
    def player_collision(self):
        x,y,w,h = self.p1.position()
        if self.center[0]<x+w and self.center[0] >x and self.center[1]+self.radius+self.speed_y>y:
             return True
    
    # checks If  ball collides with player paddle
    def cpu_collision(self):
        x,y,w,h = self.p2.position()
        if self.center[0]<x+w and self.center[0] >x and self.center[1]-self.radius+self.speed_y<y+h:
            return True



if __name__== "__main__":
    
    speed=(5,5) # initial Speed
     
    # Initialize Paddles and Balls
    p1=Paddle(screen,initial_position_player,Stride)
    c1=Paddle(screen,initial_position_cpu,Stride)
    b1=Ball(screen,center_table,speed,p1,c1)
    while not done:
            
            # Conditions for Key Presses
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
            pressed=pygame.key.get_pressed() 
            if pressed[pygame.K_LEFT]:
                p1.move_left()
            if pressed[pygame.K_RIGHT]:
                p1.move_right()
            if pressed[pygame.K_a]:
                c1.move_left()
            if pressed[pygame.K_d]:
                c1.move_right()
                    
            # set screem color
            screen.fill((0,0,0))
            if is_blue: color = (0, 128, 255)
            else: color = (255, 100, 0)

            # Draw Paddle and  Start the motion of Ball
            p1.draw()
            c1.draw()
            b1.move()
            
            # createthe surface and setting value
            s = pygame.Surface((800,600))  # the size of your rect
            s.set_alpha(128)               # alpha level
            s.fill((255,255,0))           # this fills the entire surface
            screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
            
            # if ball leaves the table reinitilize the motion of ball 
            if not b1.ball_on_table():
                done=True


            print(str(p1.score) +" - " + str(c1.score)) # print score

            # Draw table 
            pygame.display.flip()
            clock.tick(60)