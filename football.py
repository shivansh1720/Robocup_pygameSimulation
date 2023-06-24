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
screenWidth=1000
screenHeight=800
fps=30
i=0
w=0.1
exit=False
velocity=10
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

def makeField():
    pygame.draw.rect(gameWindow,white,(border,border,screenWidth-2*border,screenHeight-2*border))
    pygame.draw.rect(gameWindow,green,(border+width,border+width,screenWidth-2*border-2*width,screenHeight-2*border-2*width))
    pygame.draw.circle(gameWindow,white,(screenWidth/2,screenHeight/2),circleRad)
    pygame.draw.circle(gameWindow,green,(screenWidth/2,screenHeight/2),circleRad-width)

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

player=[bots(150,200,0),bots(150,250,0),bots(150,300,0),bots(150,350,0),bots(150,400,0)]
football=ball(screenWidth/2,screenHeight/2)

while not exit:
    gameWindow.fill(green)
    makeField()
    clock.tick(fps)
    for i in range(5):
        player[i].show()
    football.showBall()
    player[t].mark()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c and ((((football.x-player[t].x)**2)+((football.y-player[t].y)**2))**0.5)<=((botRadius*2)+10):
                player[t].catch=1
            elif event.key==pygame.K_UP:
                t=(t-1)%5
            elif event.key==pygame.K_DOWN:
                t=(t+1)%5
            elif event.key==pygame.K_h and player[t].catch==1:
                player[t].catch=0
                football.vel=fastBall
                football.theta=player[t].theta
            elif event.key==pygame.K_l and player[t].catch==1:
                player[t].catch=0
                football.vel=slowBall
                football.theta=player[t].theta

    if player[t].catch==1:
        football.x=player[t].x+botRadius*2*math.cos(player[t].theta)
        football.y=player[t].y+botRadius*2*math.sin(player[t].theta)
        # football.showBall()

    football.x+=football.vel*math.cos(football.theta)
    football.y+=football.vel*math.sin(football.theta)
    football.vel=max(football.vel-acc,0)
    # print(player.catch)
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        player[t].theta+=w
        player[t].vx=velocity*math.cos(player[t].theta)
        player[t].vy=velocity*math.sin(player[t].theta)
    elif key[pygame.K_LEFT]:
        player[t].theta-=w
        player[t].vx=velocity*math.cos(player[t].theta)
        player[t].vy=velocity*math.sin(player[t].theta)
    elif key[pygame.K_w]:
        player[t].x+=player[t].vx
        player[t].y+=player[t].vy
    elif key[pygame.K_s]:
        player[t].x-=player.vx
        player[t].y-=player[t].vy
    elif key[pygame.K_a]:
        player[t].x+=player[t].vy
        player[t].y-=player[t].vx
    elif key[pygame.K_d]:
        player[t].x-=player[t].vy
        player[t].y+=player[t].vx
    
