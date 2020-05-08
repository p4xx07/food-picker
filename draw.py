import pygame 
from random import randint
import time
import threading
import math

canvasWidth = 650
canvasHeight  = 650
white = (255, 255, 255)
iteration = 0

def init():
    pygame.init() 
    screen = pygame.display.set_mode((canvasWidth, canvasHeight))  
    pygame.display.set_caption("Tree") 
    lineHeight = 100
    screen.fill((0,0,0))  
    draw((canvasWidth / 2, canvasHeight), lineHeight, 270, screen)
    
    global iteration
    pygame.image.save(screen,"img/img"+str(iteration+1)+".jpg")
    pygame.image.save(screen,"img/img"+str(iteration+2)+".jpg")
    pygame.image.save(screen,"img/img"+str(iteration+3)+".jpg")
    pygame.image.save(screen,"img/img"+str(iteration+4)+".jpg")
    pygame.image.save(screen,"img/img"+str(iteration+5)+".jpg")
    
    iteration = 0
    pygame.quit()
  
def draw(line, height, angle, screen):
    x = line[0] + math.cos(math.radians(angle)) * height
    y = line[1] + math.sin(math.radians(angle)) * height
    pygame.draw.line(screen, white, line, (x, y), 1) 
    pygame.display.update()
    global iteration
    iteration += 1
    pygame.image.save(screen,"img/img"+str(iteration)+".jpg")

    height *=  randint(50, 80) / 100
    xAngle = angle + randint(10,45)
    yAngle = angle - randint(10,45)
    
    if(height > 5):
        draw((x,y), height, xAngle, screen)
        draw((x,y), height, yAngle, screen)

def join():
    import os
    os.system("sudo ffmpeg -f image2 -i img/img%d.jpg tree.gif")

def generateTree():
    init()
    join()


