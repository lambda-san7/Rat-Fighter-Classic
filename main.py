import pygame
from pygame import font
import time
import os
import random
from window import window
from default import dir_path
from default import fps
from default import running
from interface import scoreBox
import map
from map import stage
from map import sky_islands, italy, underworld
stage.setStage(sky_islands)
from character import rosterFrame
from character import no_char, michael, bell, gus, draedon, dante
from character import player1, player2
from interface import hp_1, hp_2
from character import rosterFrame
from interface import scoreBox
from camera import camera
from default import clock, delta
import default

stage.setStage(italy)

player1.setCharacter(no_char)
player2.setCharacter(no_char)

pygame.mouse.set_visible(False)

running = True



cursor = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/cursor.gif").convert_alpha(), (25,25))

cursorClick = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/cursorClick.gif").convert_alpha(), (25,25))

title = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/Title.gif").convert_alpha(), (300,150))

cursorSprite = None

button = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/button.gif").convert_alpha(),(292,60))
rosterselect = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/rosterselect.gif").convert_alpha(),(292,292))
rosterBack = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/rosterBack.gif").convert_alpha(),(740,500))

current_character_1 = no_char
current_character_2 = no_char

#########################
# SCENES
#########################

scene = None

class main_menu:
    def handle():
        global running
        window.fill((50,50,50))
        window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        
        window.blit(title, (10, 10))
        window.blit(button, (10, 220))
        play = text(size=36,text="Join")
        play.render(20, 240)
        global scene
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 220 + 60 and
            pygame.mouse.get_pos()[1] > 220):
                scene = roster
                
        window.blit(button, (10,280))
        play = text(size=36,text="Host")
        play.render(20,300)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 280 + 60 and
            pygame.mouse.get_pos()[1] > 280):
                scene = roster
                
        window.blit(button, (10,340))
        play = text(size=36,text="Training")
        play.render(20,360)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 340 + 60 and
            pygame.mouse.get_pos()[1] > 340):
                scene = roster
        
        window.blit(button, (10,400))
        play = text(size=36,text="Quit")
        play.render(20,420)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 400 + 60 and
            pygame.mouse.get_pos()[1] > 400):
                running = False
                

class roster:
    def handle():
        global current_character_1
        global current_character_2
        global scene
        window.fill((50,50,50))
        window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        
        window.blit(button, (10, 10))
        play = text(size=36,text="Back")
        play.render(30, 30)
        if pygame.mouse.get_pressed()[0]:
            if ((pygame.mouse.get_pos()[0] + 20) < 10 + 292 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 10 + 60 and
            pygame.mouse.get_pos()[1] > 10):
                scene = main_menu

        #window.blit(rosterBack, ((3 * 120) - 20,(.5 * 120) - 20))

        pygame.draw.rect(window, (50,50,50), (3 * 120,.5 * 120, 100, 100))
        window.blit(michael.sprites.roster, (3 * 120,.5 * 120))
        window.blit(rosterFrame, (3 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 3 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 3 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked mike")
                current_character_1 = michael
                #match.player1Char = "michael"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 3 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 3 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked mike")
                current_character_2 = michael
                #match.player2Char = "michael"

        pygame.draw.rect(window, (50,50,50), (4 * 120,.5 * 120, 100, 100))
        window.blit(bell.sprites.roster, (4 * 120,.5 * 120))
        window.blit(rosterFrame, (4 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 4 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 4 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked bell")
                current_character_1 = bell
                #match.player1Char = "bell"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 4 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 4 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked bell")
                current_character_2 = bell
                #match.player2Char = "bell"

        pygame.draw.rect(window, (50,50,50), (5 * 120,.5 * 120, 100, 100))
        window.blit(gus.sprites.roster, (5 * 120,.5 * 120))
        window.blit(rosterFrame, (5 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 5 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 5 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_1 = gus
                #match.player1Char = "gus"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 5 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 5 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_2 = gus
                #match.player2Char = "gus"
        
        pygame.draw.rect(window, (50,50,50), (6 * 120,.5 * 120, 100, 100))
        window.blit(draedon.sprites.roster, (6 * 120,.5 * 120))
        window.blit(rosterFrame, (6 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 6 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 6 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_1 = draedon
                #match.player1Char = "gus"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 6 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 6 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_2 = draedon
                #match.player2Char = "gus"

        pygame.draw.rect(window, (50,50,50), (7 * 120,.5 * 120, 100, 100))
        window.blit(dante.sprites.roster, (7 * 120,.5 * 120))
        window.blit(rosterFrame, (7 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 7 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 7 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_1 = dante
                #match.player1Char = "gus"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 7 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 7 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_2 = dante
                #match.player2Char = "gus"

        window.blit(rosterFrame, (8 * 120,.5 * 120))

        window.blit(rosterselect, (3 * 120, ((pygame.display.Info().current_h - 292) - 150) + 60))
        window.blit(current_character_1.sprites.rosterSelect,(((3 * 120) + 10) + 60, (((pygame.display.Info().current_h - 292) - 150) + 60) + 20))
        window.blit(current_character_1.sprites.idle_right,(((3 * 120) + 30, (pygame.display.Info().current_h - 260) + 60)))
        window.blit(current_character_1.hat,((3 * 120) + 50, ((pygame.display.Info().current_h - 260) + 60) - 20))
        play = text(size=36,text=f"{current_character_1.name}")
        play.render((3 * 120) + 10, (pygame.display.Info().current_h - 150) + 10)

        window.blit(rosterselect, (7 * 120, ((pygame.display.Info().current_h - 292) - 150) + 60))
        window.blit(current_character_2.sprites.rosterSelect,(((7 * 120) + 10) + 60,(((pygame.display.Info().current_h - 292) - 150) + 60) + 20))
        window.blit(current_character_2.sprites.idle_right,(((7 * 120) + 30, (pygame.display.Info().current_h - 260) + 60)))
        window.blit(current_character_2.hat,((7 * 120) + 50, ((pygame.display.Info().current_h - 260) + 60) - 20))
        play = text(size=36,text=f"{current_character_2.name}")
        play.render((7 * 120) + 10, (pygame.display.Info().current_h - 150) + 10)

        window.blit(button, (pygame.display.Info().current_w - 302, pygame.display.Info().current_h - 70))
        play = text(size=36,text="Start")
        play.render(pygame.display.Info().current_w - 292, pygame.display.Info().current_h - 60)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < pygame.display.Info().current_w - 292 + 292 and
            pygame.mouse.get_pos()[0] > pygame.display.Info().current_w - 292 and
            pygame.mouse.get_pos()[1] < pygame.display.Info().current_h - 60 + 60 and
            pygame.mouse.get_pos()[1] > pygame.display.Info().current_h - 60):
                if current_character_1 == no_char or current_character_2 == no_char:
                    return
                player1.setCharacter(current_character_1)
                player2.setCharacter(current_character_2)
                scene = game

class win_screen:
    def __init__(self, winner):
        self.winner = winner
    def handle(self):
        global running
        global scene
        window.fill((50,50,50))
        window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        
        window.blit(rosterselect, ((pygame.display.Info().current_w / 2) - 146, ((pygame.display.Info().current_h - 250) - 292) + 60))
        play = text(size=36,text=f"{self.winner.character.name} ({self.winner.name}) Wins!")
        play.render(((pygame.display.Info().current_w / 2) - 146) + 10, (pygame.display.Info().current_h - 250) + 10)
        
        window.blit(pygame.transform.scale(self.winner.character.sprites.idle_right,(200,200)),((pygame.display.Info().current_w / 2) - 100, pygame.display.Info().current_h - 450))
        window.blit(pygame.transform.scale(self.winner.character.hat,(80,80)),(((pygame.display.Info().current_w / 2) - 100, pygame.display.Info().current_h - 492)))
        window.blit(button, ((pygame.display.Info().current_w / 2) - 146, pygame.display.Info().current_h - 150))
        play = text(size=36,text=f"Continue")
        play.render(((pygame.display.Info().current_w / 2) - 146) + 10, (pygame.display.Info().current_h - 150) + 10)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < (pygame.display.Info().current_w / 2) - 146 + 292 and
            pygame.mouse.get_pos()[0] > (pygame.display.Info().current_w / 2) - 146 and 
            pygame.mouse.get_pos()[1] < pygame.display.Info().current_h - 150 + 60 and
            pygame.mouse.get_pos()[1] > pygame.display.Info().current_h - 150):
                scene = roster

class game:
    def handle():
        global scene
        if player1.character.stock <= 0:
            if player2.character.stock <= 0:
                print("draw")
                scene = roster
            winner = win_screen(player2)
            #print("player2 Wins!!!")
            scene = winner
            player1.character.stock = 3
            player2.character.stock = 3
            camera.shake_frame = 0
        if player2.character.stock <= 0:
            if player1.character.stock <= 0:
                print("draw")
            winner = win_screen(player1)
            #print("player1 Wins!!!")
            scene = winner
            player1.character.stock = 3
            player2.character.stock = 3
            camera.shake_frame = 0
            
        #print(camera.shake_frame)
        
        ##print(midpoint(player1.character.x,player1.character.y - 200,player2.character.x,player2.character.y - 200))
        #x_mid = ((stage.stage.x + stage.stage.w / 2) + player1.character.x + player2.character.x) / 3
        #y_mid = (stage.stage.y + player1.character.y + player2.character.y) / 3
        #camera.x, camera.y = midpoint(player1.character.x,player1.character.y - 200,player2.character.x,player2.character.y - 200)
        #camera.x, camera.y = x_mid - (pygame.display.Info().current_w / 2), y_mid - (100) - (pygame.display.Info().current_h / 2)
        
        stage.handle()
        if camera.shake_frame > 0:
            pygame.draw.rect(window, (0,0,0), (0, 0, pygame.display.Info().current_w, random.randint(1,25)))
            pygame.draw.rect(window, (0,0,0), (0, pygame.display.Info().current_h - random.randint(1,25), pygame.display.Info().current_w, 20))
            camera.x += random.randint(-10, 10)
            camera.y += random.randint(-10, 10)

            pygame.display.update

            time.sleep(.02)

            camera.shake_frame -= 1
        if camera.shake_frame <= 0:
            camera.x, camera.y = ((stage.stage.x + stage.stage.w) / 2) - (pygame.display.Info().current_w / 2), (stage.stage.y - (pygame.display.Info().current_w / 2)) + 200
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
        score = text(size=36,text=f"{player1.character.stock}/{player2.character.stock}")
        score.render((pygame.display.Info().current_w - score.text.get_width()) / 2, 13)


class text:
    def __init__(self, size, text):
        self.font = pygame.font.Font(f"{dir_path}/font.fon",size)
        self.text_holder = text
        self.text = self.font.render(text, True, (255,255,255))
    def render(self,x,y):
        font = pygame.font.Font(f"{dir_path}/font.fon",32)
        text = font.render(self.text_holder, True, (0,0,0))
        window.blit(text,(x + 2,y))
        window.blit(text,(x - 2,y))
        window.blit(text,(x,y + 2))

        window.blit(text,(x,y - 2))

        window.blit(text,(x + 2,y + 2))
        window.blit(text,(x - 2,y + 2))
        window.blit(text,(x - 2,y - 2))
        window.blit(text,(x + 2,y - 2))

        window.blit(self.text,(x,y))

scene = main_menu

cursorSprite = cursor

while running:
    #default.delta = clock.tick(fps)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    scene.handle()
    window.blit(cursorSprite, pygame.mouse.get_pos())
    pygame.display.update()

pygame.quit