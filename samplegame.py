import pygame
import math
pygame.init()

# Colours
white=(255,255,255)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,255)
black=(0,0,0)
yellow=(255,255,0)

# Creating window
screenWidth=1200
screenHeight=800
fps=60
i=0
w=0.1
exit=False
velocity=5
slowBall=20
fastBall=40
acc=5
circleRad=100
clock=pygame.time.Clock()
gameWindow=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Let's football")
pygame.display.update()

t=0
botRadius=20
border=100
width=7

o = 50
width, height = 1200,800
f_width, f_height = 1100,700
D_yposition = 177.5
G_yposition = 252.5
D_r_xposition = 875
G_r_xposition = 1025
thickness = 6.25
D_width = 112.5
D_length = 345
G_width = 37.5
G_length = 195

def makeField():
    border_c = pygame.Rect(width/2 - thickness/2 + 1, o , thickness , height - 2*o)
    border_fl = pygame.Rect(o , o , thickness , height - 2*o)
    border_fr = pygame.Rect(f_width + o + 1 - thickness , o , thickness , height - 100)
    border_fu = pygame.Rect(o , o , width - 2*o , thickness)
    border_fd = pygame.Rect(o , f_height + o + 1 - thickness , width - 2*o , thickness)
    goall_1_u = pygame.Rect(o , o + D_yposition , D_width , thickness)
    goall_1_d = pygame.Rect(o , o + D_length + D_yposition , D_width , thickness)
    goall_1_l = pygame.Rect(o + D_width , o + D_yposition , thickness , D_length+thickness )
    goall_2_u = pygame.Rect(o , o + G_yposition, G_width , thickness)
    goall_2_d = pygame.Rect(o , o + G_yposition + G_length , G_width , thickness)
    goall_2_l = pygame.Rect(o + G_width , o + G_yposition , thickness , G_length + thickness)
    goalr_1_u = pygame.Rect(o + D_width + D_r_xposition, o + D_yposition , D_width , thickness)
    goalr_1_d = pygame.Rect(o + D_width + D_r_xposition, o + D_length + D_yposition , D_width , thickness)
    goalr_1_l = pygame.Rect(o + D_width + D_r_xposition, o + D_yposition , thickness , D_length + thickness )
    goalr_2_u = pygame.Rect(o + G_width + G_r_xposition , o + G_yposition , G_width , thickness)
    goalr_2_d = pygame.Rect(o + G_width + G_r_xposition , o + G_yposition + G_length , G_width , thickness)
    goalr_2_l = pygame.Rect(o + G_width + G_r_xposition , o + G_yposition , thickness , G_length + thickness)

    pygame.draw.rect(gameWindow,white,border_c)
    pygame.draw.rect(gameWindow,white,border_fl)
    pygame.draw.rect(gameWindow,white,border_fr)
    pygame.draw.rect(gameWindow,white,border_fu)
    pygame.draw.rect(gameWindow,white,border_fd)
    pygame.draw.circle(gameWindow, white, (600, 400), 50 , 6)
    pygame.draw.circle(gameWindow, white, (600, 400), 6)
    pygame.draw.circle(gameWindow, white, (230, 400), 6)
    pygame.draw.circle(gameWindow, white, (970, 400), 6)
    pygame.draw.arc(gameWindow, white, pygame.Rect(o - 37 , o - 37 , 74 , 74), math.radians(270), math.radians(360), 6)
    pygame.draw.arc(gameWindow, white, pygame.Rect(o + f_width - 37 , o - 37 , 74 , 74), math.radians(180), math.radians(270), 6)
    pygame.draw.arc(gameWindow, white, pygame.Rect(o - 37 , o + f_height - 37 , 74 , 74), math.radians(0), math.radians(90), 6)
    pygame.draw.arc(gameWindow, white, pygame.Rect(o + f_width - 37 , o +f_height - 37 , 74 , 74), math.radians(90), math.radians(180), 6)
    pygame.draw.rect(gameWindow,white, goall_1_u)
    pygame.draw.rect(gameWindow,white, goall_1_d)
    pygame.draw.rect(gameWindow,white, goall_1_l)
    pygame.draw.rect(gameWindow,white, goall_2_u)
    pygame.draw.rect(gameWindow,white, goall_2_d)
    pygame.draw.rect(gameWindow,white, goall_2_l)
    pygame.draw.rect(gameWindow,white, goalr_1_u)
    pygame.draw.rect(gameWindow,white, goalr_1_d)
    pygame.draw.rect(gameWindow,white, goalr_1_l)
    pygame.draw.rect(gameWindow,white, goalr_2_u)
    pygame.draw.rect(gameWindow,white, goalr_2_d)
    pygame.draw.rect(gameWindow,white, goalr_2_l)

class goalKeeper:
    def __init__(self,x,theta):
        self.y=screenHeight/2
        self.x=x
        self.theta=theta
    def show(self):
        pygame.draw.circle(gameWindow,blue,(self.x,self.y),botRadius)
        pygame.draw.circle(gameWindow,white,(self.x+(botRadius-6)*math.cos(self.theta),self.y+(botRadius-6)*math.sin(self.theta)),5)

class bots:
    def __init__(self,xPos,yPos,theta):
        self.x=xPos
        self.y=yPos
        self.theta=theta
        self.vx=velocity*math.cos(theta)
        self.vy=velocity*math.sin(theta)
        self.catch=0
    def show(self):
        pygame.draw.circle(gameWindow,red,(self.x,self.y),botRadius)
        pygame.draw.circle(gameWindow,white,(self.x+(botRadius-6)*math.cos(self.theta),self.y+(botRadius-6)*math.sin(self.theta)),5)
        # pygame.display.update()
    def mark(self):
        pygame.draw.circle(gameWindow,blue,(self.x,self.y),10)
    def boundary(self):
        if self.x>=screenWidth:
            self.x=screenWidth
        if self.x<=0:
            self.x=0
        if self.y>=screenHeight:
            self.y=screenHeight
        if self.y<=0:
            self.y=0
    
# ballX=screenWidth/2
# bally=screenHeight/2
class ball:
    def __init__(self,ballx,bally):
        self.x=ballx
        self.y=bally
        self.vel=0
        self.ax=0
        self.ay=0
        self.theta=0
    def showBall(self):
        pygame.draw.circle(gameWindow,white,(self.x,self.y),botRadius)
        pygame.draw.circle(gameWindow,black,(self.x,self.y),botRadius-5)

        # pygame.draw.circle(gameWindow,white,(self.x+botRadius*math.cos(self.theta)/2,self.y+botRadius*math.sin(self.theta)/2),5)
        # pygame.display.update()

player=[bots(300,300,0),bots(300,350,0),bots(300,400,0),bots(300,450,0),bots(300,500,0)]
keeper=[goalKeeper(o,0),goalKeeper(screenWidth-o,91)]
football=ball(screenWidth/2,screenHeight/2)

throw=0

while not exit:
    gameWindow.fill(green)
    makeField()
    clock.tick(fps)
    for i in range(5):
        player[i].show()
    football.showBall()
    player[t].mark()
    keeper[0].show()
    keeper[1].show()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_h and player[t].catch==1:
                player[t].catch=0
                football.vel=fastBall
                football.theta=player[t].theta
                throw=t
            elif event.key==pygame.K_l and player[t].catch==1:
                player[t].catch=0
                football.vel=slowBall
                football.theta=player[t].theta
                throw=t
            elif event.key==pygame.K_UP:
                t=(t-1)%5
            elif event.key==pygame.K_DOWN:
                t=(t+1)%5
            # else:
                # mark=0
                # flag=0
                # for i in range(5):
                #     if (((((football.x-player[i].x)**2)+((football.y-player[i].y)**2))**0.5)<=((botRadius*2)+10)):
                #         mark=i
                #         flag=1
                #         break
                # if flag==1:
                #     player[t].catch=0
                #     player[mark].catch=1
                #     t=mark


    mark=0
    flag=0
    count=0
    for i in range(5):
        if player[i].catch==0:
            count+=1
    if count==5:
        for i in range(5):
            if football.vel!=0 and i==throw:
                continue
            if (((((football.x-player[i].x)**2)+((football.y-player[i].y)**2))**0.5)<=((botRadius*2)+10)):
                t=i
                player[t].catch=1
                break

    for i in range(5):
        if i==t:
            continue
        elif (((((football.x-player[i].x)**2)+((football.y-player[i].y)**2))**0.5)<=((botRadius*2)+10)):
            mark=i
            flag=1
            break
    if flag==1:
        player[t].catch=0
        player[mark].catch=1
        t=mark
            

    if player[t].catch==1:
        football.x=player[t].x+botRadius*2*math.cos(player[t].theta)
        football.y=player[t].y+botRadius*2*math.sin(player[t].theta)
        # football.showBall()

    if football.x>=screenWidth:
        football.x=screenWidth
    if football.x<=0:
        football.x=0
    if football.y>=screenHeight:
        football.y=screenHeight
    if football.y<=0:
        football.y=0
    football.x+=football.vel*math.cos(football.theta)
    football.y+=football.vel*math.sin(football.theta)
    football.vel=max(football.vel-acc,0)
    # print(player.catch)
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        player[t].theta+=w
        player[t].vx=velocity*math.cos(player[t].theta)
        player[t].vy=velocity*math.sin(player[t].theta)
        player[t].boundary()
    elif key[pygame.K_LEFT]:
        player[t].theta-=w
        player[t].vx=velocity*math.cos(player[t].theta)
        player[t].vy=velocity*math.sin(player[t].theta)
        player[t].boundary()
    elif key[pygame.K_w]:
        player[t].x+=player[t].vx
        player[t].y+=player[t].vy
        player[t].boundary()
    elif key[pygame.K_s]:
        player[t].x-=player[t].vx
        player[t].y-=player[t].vy
        player[t].boundary()
    elif key[pygame.K_a]:
        player[t].x+=player[t].vy
        player[t].y-=player[t].vx
        player[t].boundary()
    elif key[pygame.K_d]:
        player[t].x-=player[t].vy
        player[t].y+=player[t].vx
        player[t].boundary()
    
