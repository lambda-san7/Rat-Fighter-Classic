import pygame
from window import window
from window import height, width
from default import dir_path
import camera
from camera import camera as cam

hpFrame = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/hpframe.gif").convert_alpha(),(500,20))
scoreBox = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/score inbetween hps.gif").convert_alpha(),(146,30))

class bar:
    
    #################### BACKGROUND BAR ####################

    class emptySpace:
        def __init__(self,x,y,w,h,color):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.color = color

    #################### FOREGROUND BAR ####################

    def __init__(self,x,y,w,h,color,color2):
        self.empty = self.emptySpace(x,y,w,h,color2)
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.color = color

    #################### RENDER ####################

    def render(self):
        self.x = self.x
        pygame.draw.rect(window, self.empty.color, pygame.Rect(self.empty.x, self.empty.y, self.empty.w, self.empty.h))
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
        #window.blit(hpFrame, (self.empty.x,self.empty.y))
        
#########################
# BARS
#########################

hp_1 = bar(
    x=110,
    y=10,
    w=500,
    h=20,
    color=(255,255,0),
    color2=(128,128,128),
)

hp_2 = bar(
    x=pygame.display.Info().current_w - 610,
    y=10,
    w=500,
    h=20,
    color=(255,255,0),
    color2=(128,128,128),
)