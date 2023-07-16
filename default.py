import pygame
import os
from window import width, height

running = True

fps = 60

gravityAffected = []

pygame.init()

def midpoint(x1,y1,x2,y2):
    x = x2 + x1
    y = y2 + y1
    x /= 2
    y /= 2
    return x - (width / 2),y - (height / 2)

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

clock = pygame.time.Clock()

delta = clock.tick(fps)/1000

pygame_icon = pygame.image.load(f"{dir_path}/michael/idle_left.gif").convert_alpha()
pygame.display.set_icon(pygame_icon)