#########################
# IMPORTS
#########################

import pygame
#import main
from window import window
from default import dir_path
from default import fps
from default import running
from interface import scoreBox
import match as game_match
from match import player1Char, player2Char, stage
from pygame import font

pygame.mouse.set_visible(False)

game_match.player1Char = "gus"
game_match.player2Char = "bell"
game_match.stage = "sky_islands"

button = pygame.transform.scale(pygame.image.load(f"{dir_path}/score inbetween hps.gif").convert_alpha(),(292,60))

pygame.font.init()

#########################
# TEXT
#########################

class text:
    def __init__(self, size, text):
        self.font = pygame.font.Font(f"{dir_path}/font.fon",size)
        self.text = self.font.render(text, True, (255,255,255))
    def render(self,x,y):
        window.blit(self.text,(x,y)) # (self.x,self.y)
        
#########################
# SCENES
#########################

class main_menu:
    def handle():
        window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        #window.fill((50,50,50))
        window.blit(title, (10, 10))
        window.blit(button, (10, 220))
        play = text(size=36,text="Join")
        play.render(20, 240)
        if pygame.mouse.get_pressed()[0]:
            if ((pygame.mouse.get_pos()[0] + 20) < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 220 + 30 and
            pygame.mouse.get_pos()[1] > 220):
                import main
        window.blit(button, (10,280))
        play = text(size=36,text="Host")
        play.render(20,300)
        if pygame.mouse.get_pressed()[0]:
            if ((pygame.mouse.get_pos()[0] + 20) < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 280 + 30 and
            pygame.mouse.get_pos()[1] > 280):
                import main
        window.blit(button, (10,340))
        play = text(size=36,text="Training")
        play.render(20,360)
        if pygame.mouse.get_pressed()[0]:
            if ((pygame.mouse.get_pos()[0] + 20) < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 340 + 30 and
            pygame.mouse.get_pos()[1] > 340):
                import main
        
        


#########################
# GAME LOOP
#########################

#################### TICKER ####################

clock = pygame.time.Clock()

cursor = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursor.gif").convert_alpha(), (25,25))

cursorClick = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursorClick.gif").convert_alpha(), (25,25))

title = pygame.transform.scale(pygame.image.load(f"{dir_path}/Title.gif").convert_alpha(), (300,150))

cursorSprite = None

scene = main_menu

#################### LOOP ####################

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    #if pygame.mouse.get_pressed()[0]:
        
    cursorSprite = cursor
    scene.handle()
    window.blit(cursorSprite, pygame.mouse.get_pos())
    pygame.display.update()

pygame.quit