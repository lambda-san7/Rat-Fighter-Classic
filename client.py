#########################
# IMPORTS
#########################

import pygame
#import main
import time
from window import window
from default import dir_path
from default import fps
from default import running
from interface import scoreBox
import match as game_match
from match import player1Char, player2Char, stage
from pygame import font
from character import rosterFrame
from character import no_char, michael, bell, gus

pygame.mouse.set_visible(False)


game_match.player2Char = "bell"
game_match.stage = "sky_islands"

button = pygame.transform.scale(pygame.image.load(f"{dir_path}/score inbetween hps.gif").convert_alpha(),(292,60))

current_character = no_char

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

scene = None

class main_menu:
    def handle():
        #window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        window.fill((50,50,50))
        window.blit(title, (10, 10))
        window.blit(button, (10, 220))
        play = text(size=36,text="Join")
        play.render(20, 240)
        global scene
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 220 + 60 and
            pygame.mouse.get_pos()[1] > 220):
                scene = roster
                
        window.blit(button, (10,280))
        play = text(size=36,text="Host")
        play.render(20,300)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 280 + 60 and
            pygame.mouse.get_pos()[1] > 280):
                scene = roster
                
        window.blit(button, (10,340))
        play = text(size=36,text="Training")
        play.render(20,360)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 340 + 60 and
            pygame.mouse.get_pos()[1] > 340):
                scene = roster
                

class roster:
    def handle():
        global current_character
        global scene
        #window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        window.fill((50,50,50))
        window.blit(button, (10, 10))
        play = text(size=36,text="Back")
        play.render(30, 30)
        if pygame.mouse.get_pressed()[0]:
            if ((pygame.mouse.get_pos()[0] + 20) < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 10 + 60 and
            pygame.mouse.get_pos()[1] > 10):
                scene = main_menu

        window.blit(michael.sprites.roster, (3 * 120,.5 * 120))
        window.blit(rosterFrame, (3 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 3 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 3 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                print("clicked mike")
                current_character = michael
                game_match.player1Char = "michael"

        window.blit(bell.sprites.roster, (4 * 120,.5 * 120))
        window.blit(rosterFrame, (4 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 4 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 4 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                print("clicked bell")
                current_character = bell
                game_match.player1Char = "bell"

        window.blit(gus.sprites.roster, (5 * 120,.5 * 120))
        window.blit(rosterFrame, (5 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 5 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 5 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                print("clicked gus")
                current_character = gus
                game_match.player1Char = "gus"

        window.blit(rosterFrame, (6 * 120,.5 * 120))

        window.blit(rosterFrame, (7 * 120,.5 * 120))

        window.blit(rosterFrame, (8 * 120,.5 * 120))

        window.blit(pygame.transform.scale(current_character.sprites.idle_right,(100,100)),(3 * 120, pygame.display.Info().current_h - 250))
        window.blit(pygame.transform.scale(current_character.hat,(50,50)),((3 * 120) + 50, pygame.display.Info().current_h - 292))
        window.blit(button, (3 * 120, pygame.display.Info().current_h - 150))
        play = text(size=36,text=f"{current_character.name}")
        play.render((3 * 120) + 10, (pygame.display.Info().current_h - 150) + 10)

        window.blit(button, (pygame.display.Info().current_w - 302, pygame.display.Info().current_h - 70))
        play = text(size=36,text="Start")
        play.render(pygame.display.Info().current_w - 292, pygame.display.Info().current_h - 60)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < pygame.display.Info().current_w - 292 + 292 and
            pygame.mouse.get_pos()[0] > pygame.display.Info().current_w - 292 and
            pygame.mouse.get_pos()[1] < pygame.display.Info().current_h - 60 + 60 and
            pygame.mouse.get_pos()[1] > pygame.display.Info().current_h - 60):
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

running2 = True

#################### LOOP ####################

while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False
    clock.tick(60)
    #if pygame.mouse.get_pressed()[0]:
        
    cursorSprite = cursor
    scene.handle()
    window.blit(cursorSprite, pygame.mouse.get_pos())
    pygame.display.update()

pygame.quit