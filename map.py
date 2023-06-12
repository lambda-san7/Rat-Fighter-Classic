import pygame
from window import window
from camera import camera
#from match import stage as matchStage

class map:
    def __init__(self,location=[0,100],size=[400,240],sprite="map_assets/Floor2.gif",backdrop="map_assets/Sky.gif",extra="map_assets/extra.gif"):
        self.x = location[0]
        self.y = location[1]
        self.w = size[0]
        self.h = size[1]
        self.sprite = pygame.transform.scale(pygame.image.load(sprite).convert_alpha(),(self.w,self.h))
        self.extra = pygame.transform.scale(pygame.image.load(extra).convert_alpha(),(self.w,1000))
        self.backdrop = pygame.transform.scale(pygame.image.load(backdrop),(pygame.display.Info().current_w,pygame.display.Info().current_h))
    def render(self):
        self.sprite = pygame.transform.scale(self.sprite,(self.w * camera.scale,self.h * camera.scale))
        window.blit(self.backdrop,(0,0))
        window.blit(self.sprite,((self.x - camera.x) * camera.scale,(self.y - camera.y) * camera.scale))
        window.blit(self.extra,((self.x - camera.x) * camera.scale,((self.y - 999) - camera.y) * camera.scale))

#################### SKY ISLANDS ####################

sky_islands = map(
    sprite="map_assets/Floor.gif",
    backdrop="map_assets/Sky.png",
)

#################### UNDERWORLD ####################

underworld = map(
    sprite="map_assets/Floor2.gif",
    backdrop="map_assets/cavern.png",
    extra="map_assets/extra2.gif"
)

italy = map(
    size=[400,800],
    sprite="map_assets/image.gif",
    backdrop="map_assets/venice_sky.png",
    extra="map_assets/venice_extra.gif"
)

class new_stage:
    def __init__(self):
        self.stage = None
    def setStage(self,stage):
        self.stage = stage
    def handle(self):
        self.stage.render()

#################### PLAYERS 1 & 2 ####################

stage = new_stage()