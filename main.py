#########################
# IMPORTS
#########################

import pygame
import os
from default import dir_path
from default import midpoint
from default import gravityAffected
from default import fps
from default import running
from window import window
from window import width, height
from character import michael, bell, gus
from camera import camera
from map import stage
from map import sky_islands,underworld,italy
from sounds import italy_smooth
from interface import hp_1, hp_2
from character import rosterFrame
from interface import scoreBox
from character import hats
from match import player1Char, player2Char

pygame.mouse.set_visible(False)

#########################
# PLAYER OBJECTS
#########################

class player:
    def __init__(self,uldr,name):
        self.character = None
        self.uldr = uldr
        self.target = None
        self.name = name
    def setCharacter(self,character):
        self.character = character
        self.character.uldr = self.uldr
        self.character.target = self.target
        self.character.player = self.name
        if self.name == "player1":
            self.character.spawn_point = (stage.x, stage.y - 100)
            self.character.x, self.character.y = self.character.spawn_point
        if self.name == "player2":
            self.character.spawn_point = (stage.x + (stage.w - self.character.w), stage.y - 100)
            self.character.x, self.character.y = self.character.spawn_point
    def handleCharacter(self):
        self.character.render()
        self.character.controller()
        self.character.gravitate()
        if self.name == "player1":
            window.blit(self.character.sprites.roster, (10,10))
        if self.name == "player2":
            window.blit(self.character.sprites.roster, (pygame.display.Info().current_w - 110,10))

#################### PLAYERS 1 & 2 ####################

player1 = player([pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g],"player1")
player2 = player([pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL],"player2")

player1.target = player2
player2.target = player1

#################### SET CHARACTERS ####################

player1.setCharacter(eval(player1Char))
player2.setCharacter(eval(player2Char))

#########################
# GRAVITY
#########################

'''def gravity():
    for i in gravityAffected:
        if i.offScreen(): #checks if any rat is off the screen
            i.x, i.y = stage.x + 100,stage.y - 100
        if (i.y + 1) < stage.y + stage.h and (i.y + 1) + i.h > stage.y: # if any rat is in Y
            i.y -= i.jumpVelocity
            for o in range(2):
                i.y += 1
            i.jumpVelocity -= 1
            
            if i.x < stage.x + stage.w and i.x + i.w > stage.x: # if any rat is in X
                i.jumpVelocity = 0
                return
                i.y = stage.y - i.h'''
                
#########################
# GAME LOOP
#########################

#################### TICKER ####################

clock = pygame.time.Clock()

cursor = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursor.gif").convert_alpha(), (25,25))

cursorClick = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursorClick.gif").convert_alpha(), (25,25))

cursorSprite = None

#################### LOOP ####################

while running:
#    italy_smooth.set_volume(0.1)
 #   italy_smooth.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    cursorSprite = cursor
    #print(midpoint(player1.character.x,player1.character.y - 200,player2.character.x,player2.character.y - 200))
    #x_mid = ((stage.x + stage.w / 2) + player1.character.x + player2.character.x) / 3
    #y_mid = (stage.y + player1.character.y + player2.character.y) / 3
    #camera.x, camera.y = midpoint(player1.character.x,player1.character.y - 200,player2.character.x,player2.character.y - 200)
    #camera.x, camera.y = x_mid - (pygame.display.Info().current_w / 2), y_mid - (100) - (pygame.display.Info().current_h / 2)
    camera.x, camera.y = ((stage.x + stage.w) / 2) - (pygame.display.Info().current_w / 2), (stage.y - (pygame.display.Info().current_w / 2)) + 200
    if pygame.mouse.get_pressed()[0]:
        cursorSprite = cursorClick
    stage.render()
    hp_1.w = player1.character.health
    hp_1.render()
   # hp_2.x, hp_2.empty.x = pygame.display.Info().current_w - 610,pygame.display.Info().current_w - 610
    hp_2.w = player2.character.health
    hp_2.render()
    player2.handleCharacter()
    player1.handleCharacter()
    window.blit(rosterFrame, (10,10))
    window.blit(rosterFrame, (pygame.display.Info().current_w - 110,10))
    window.blit(scoreBox, ((pygame.display.Info().current_w - 146) / 2,10))
    window.blit(cursorSprite, pygame.mouse.get_pos())
    pygame.display.update()

pygame.quit