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

pygame.mouse.set_visible(False)

player1, player2 = "michael", "bell"
print("passed p1/2 assignment")

game_match.player1Char = "gus"
game_match.player2Char = "bell"
game_match.stage = "sky_islands"

#########################
# SCENES
#########################

class main_menu:
    def handle():
        window.fill((50,50,50))
        window.blit(scoreBox, (pygame.display.Info().current_w / 2,pygame.display.Info().current_h / 2))
        if pygame.mouse.get_pressed()[0]:
            if ((pygame.mouse.get_pos()[0] + 20) < pygame.display.Info().current_w / 2 + 146 and
            pygame.mouse.get_pos()[0] > pygame.display.Info().current_w / 2 and
            pygame.mouse.get_pos()[1] < pygame.display.Info().current_h / 2 + 30 and
            pygame.mouse.get_pos()[1] > pygame.display.Info().current_h / 2):
                import main


#########################
# GAME LOOP
#########################

#################### TICKER ####################

clock = pygame.time.Clock()

cursor = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursor.gif").convert_alpha(), (25,25))

cursorClick = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursorClick.gif").convert_alpha(), (25,25))

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