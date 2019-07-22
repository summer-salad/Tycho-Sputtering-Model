import pygame
from pygame.locals import *
import random, math, sys
import time

pygame.init()

Surface = pygame.display.set_mode((800,600))


Circles = []
class Circle:
    def __init__(self):
        #self.radius = int(random.random()*50) + 1
        self.radius = 10
        self.x = random.randint(self.radius, 800-self.radius)
        self.y = random.randint(self.radius+50, 550-self.radius)
        self.speedx = 0.5*(random.random()+1.0)
        #self.speedx = 0
        self.speedy = 0.5*(random.random()+1.0)
        #self.speedx= 0.2
        #self.speedy= 0.2
##        self.mass = math.sqrt(self.radius)
a = 200

Tcircles = []
class Tcircle:
    def __init__(self):
        self.radius = 5
        #self.x = random.randint(self.radius, 800-self.radius)
        self.x = a
        self.y = 50
        self.speedx = 0
        self.speedy = 0.5*(random.random()+1.0)

for x in range(4):
    Circles.append(Circle())

def CircleCollide(C1,C2):
    C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
    XDiff = -(C1.x-C2.x)
    YDiff = -(C1.y-C2.y)
    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    
    C1.speedx = XSpeed
    C1.speedy = YSpeed
def Move():
    for Circle in Circles:
        Circle.x += Circle.speedx
        Circle.y += Circle.speedy
def CollisionDetect():
    for Circle in Circles:
        if Circle.x < Circle.radius or Circle.x > 800-Circle.radius:    Circle.speedx *= -1
        if Circle.y < Circle.radius+50 or Circle.y > 550-Circle.radius:    Circle.speedy *= -1
        for Circle2 in Circles:
            if Circle != Circle2:
                if math.sqrt(  ((Circle.x-Circle2.x)**2)  +  ((Circle.y-Circle2.y)**2)  ) <= (Circle.radius+Circle2.radius):
                    CircleCollide(Circle,Circle2)
def Draw():
    Surface.fill((0,0,0))
    pygame.draw.rect(Surface, (150,0,0), (0, 0, 800, 50))
    pygame.draw.rect(Surface, (0,150,0), (0,550, 800, 50))
    for Circle in Circles:
        pygame.draw.circle(Surface,(0,0,150),(int(Circle.x),int(Circle.y)),Circle.radius)
    for Tcircle in Tcircles:
        pygame.draw.circle(Surface,(150,0,0),(int(Tcircle.x),int(Tcircle.y)),Tcircle.radius)
    pygame.display.flip()
def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()
def TargetCreate():
    Tcircles.append(Tcircle())
   # Tcircle.x = 100
#def TargetPosition():
 #   Tcircle.x = Circle.x
def TargetDetect():
    for Circle in Circles:
        if Circle.y < 60:
            a = 400
            TargetCreate()
            
def MoveT():
    for Tcircle in Tcircles:
        if Tcircle.y >= 550:
            Tcircle.speedx = 0
            Tcircle.speedy = 0
        '''
        for Tcircle2 in Tcircles:
            if Tcircle != Tcircle2:
                if math.sqrt(  ((Tcircle.x-Tcircle2.x)**2)  +  ((Tcircle.y-Tcircle2.y)**2)  ) <= (Tcircle.radius+Tcircle2.radius):
                    Tcircle.speedx = 0
                    Tcircle.speedy = 0
        '''
        
        Tcircle.x += Tcircle.speedx
        Tcircle.y += Tcircle.speedy

def main():
    while True:
        GetInput()
        Move()
        CollisionDetect()
        TargetDetect()
        MoveT()
        Draw()
        
       
if __name__ == '__main__': main()  
