import pygame
from camera import camera
from window import window
from window import width, height
import default
from default import dir_path
from default import gravityAffected
from map import stage
from match import player1Char, player2Char
from default import clock, delta



bubble = pygame.transform.scale(pygame.image.load(f"{dir_path}/bubble.gif").convert_alpha(),(60,60))
jump_ground = pygame.transform.scale(pygame.image.load(f"{dir_path}/jump_grounded.gif").convert_alpha(),(70,70))
pointer = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/player_pointer.gif").convert_alpha(),(20,20))

rosterFrame = pygame.transform.scale(pygame.image.load(f"{dir_path}/ui/rosterframe.gif").convert_alpha(),(100,100))


class hats:
    none = pygame.transform.scale(pygame.image.load(f"{dir_path}/none_hat.gif").convert_alpha(),(25,25))
    tophat = pygame.transform.scale(pygame.image.load(f"{dir_path}/tophat.gif").convert_alpha(),(25,25))
    chef = pygame.transform.scale(pygame.image.load(f"{dir_path}/chef.gif").convert_alpha(),(25,25))
    cowboy = pygame.transform.scale(pygame.image.load(f"{dir_path}/cowboy.gif").convert_alpha(),(25,25))
    arthur = pygame.transform.scale(pygame.image.load(f"{dir_path}/arthur_morgan.gif").convert_alpha(),(25,25))

class character:

    #################### SPRITES ####################

    class spriteList:
        def __init__(self,spriteSheet,w,h):
            
            #################### IDLE ####################

            self.idle_left = pygame.transform.scale(pygame.image.load(spriteSheet[0]).convert_alpha(),(w,h))
            self.idle_right = pygame.transform.flip(self.idle_left, True, False)

            #################### RUNNING ####################

            self.run_l_1 = pygame.transform.scale(pygame.image.load(spriteSheet[1]).convert_alpha(),(w,h))
            self.run_l_2 = pygame.transform.scale(pygame.image.load(spriteSheet[2]).convert_alpha(),(w,h))
            self.run_l_3 = pygame.transform.scale(pygame.image.load(spriteSheet[3]).convert_alpha(),(w,h))
            self.run_l_4 = pygame.transform.scale(pygame.image.load(spriteSheet[4]).convert_alpha(),(w,h))
            self.run_r_1 = pygame.transform.flip(self.run_l_1, True, False)
            self.run_r_2 = pygame.transform.flip(self.run_l_2, True, False)
            self.run_r_3 = pygame.transform.flip(self.run_l_3, True, False)
            self.run_r_4 = pygame.transform.flip(self.run_l_4, True, False)

            #################### CROUCH ####################

            self.crouch_l = pygame.transform.scale(pygame.image.load(spriteSheet[5]).convert_alpha(),(w,h))
            self.crouch_r = pygame.transform.flip(self.crouch_l, True, False)

            #################### ATTACK FX ####################

            self.attack_l_1 = pygame.transform.scale(pygame.image.load(spriteSheet[6]).convert_alpha(),(w + 30,h + 30))
            self.attack_l_2 = pygame.transform.scale(pygame.image.load(spriteSheet[7]).convert_alpha(),(w + 30,h + 30))
            self.attack_l_3 = pygame.transform.scale(pygame.image.load(spriteSheet[8]).convert_alpha(),(w + 30,h + 30))
            self.attack_l_4 = pygame.transform.scale(pygame.image.load(spriteSheet[9]).convert_alpha(),(w + 30,h + 30))
            self.attack_r_1 = pygame.transform.flip(self.attack_l_1, True, False)
            self.attack_r_2 = pygame.transform.flip(self.attack_l_2, True, False)
            self.attack_r_3 = pygame.transform.flip(self.attack_l_3, True, False)
            self.attack_r_4 = pygame.transform.flip(self.attack_l_4, True, False)

            #################### SPIN ATTACK FX ####################

            self.spin_l_1 = pygame.transform.scale(pygame.image.load(spriteSheet[10]).convert_alpha(),(w + 30,h + 30))
            self.spin_l_2 = pygame.transform.scale(pygame.image.load(spriteSheet[11]).convert_alpha(),(w + 30,h + 30))
            self.spin_l_3 = pygame.transform.scale(pygame.image.load(spriteSheet[12]).convert_alpha(),(w + 30,h + 30))
            self.spin_l_4 = pygame.transform.scale(pygame.image.load(spriteSheet[13]).convert_alpha(),(w + 30,h + 30))
            self.spin_r_1 = pygame.transform.flip(self.spin_l_1, True, False)
            self.spin_r_2 = pygame.transform.flip(self.spin_l_2, True, False)
            self.spin_r_3 = pygame.transform.flip(self.spin_l_3, True, False)
            self.spin_r_4 = pygame.transform.flip(self.spin_l_4, True, False)

            #################### SIDE ATTACK FX ####################

            self.side_l_1 = pygame.transform.scale(pygame.image.load(spriteSheet[14]).convert_alpha(),(w + 30,h + 30))
            self.side_l_2 = pygame.transform.scale(pygame.image.load(spriteSheet[15]).convert_alpha(),(w + 30,h + 30))
            self.side_l_3 = pygame.transform.scale(pygame.image.load(spriteSheet[16]).convert_alpha(),(w + 30,h + 30))
            self.side_l_4 = pygame.transform.scale(pygame.image.load(spriteSheet[17]).convert_alpha(),(w + 30,h + 30))
            self.side_r_1 = pygame.transform.flip(self.side_l_1, True, False)
            self.side_r_2 = pygame.transform.flip(self.side_l_2, True, False)
            self.side_r_3 = pygame.transform.flip(self.side_l_3, True, False)
            self.side_r_4 = pygame.transform.flip(self.side_l_4, True, False)

            #################### PLAYER ATTACKING ####################

            self.attacking_l_1 = pygame.transform.scale(pygame.image.load(spriteSheet[18]).convert_alpha(),(w + 30,h + 30))
            self.attacking_l_2 = pygame.transform.scale(pygame.image.load(spriteSheet[19]).convert_alpha(),(w + 30,h + 30))
            self.attacking_l_3 = pygame.transform.scale(pygame.image.load(spriteSheet[20]).convert_alpha(),(w + 30,h + 30))
            self.attacking_l_4 = pygame.transform.scale(pygame.image.load(spriteSheet[21]).convert_alpha(),(w + 30,h + 30))
            self.attacking_r_1 = pygame.transform.flip(self.attacking_l_1, True, False)
            self.attacking_r_2 = pygame.transform.flip(self.attacking_l_2, True, False)
            self.attacking_r_3 = pygame.transform.flip(self.attacking_l_3, True, False)
            self.attacking_r_4 = pygame.transform.flip(self.attacking_l_4, True, False)

            #################### GROUNDPOUND FX ####################

            self.groundpound_l_1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(spriteSheet[6]).convert_alpha(),(w + 30,h + 30)), False, True)
            self.groundpound_l_2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(spriteSheet[7]).convert_alpha(),(w + 30,h + 30)), False, True)
            self.groundpound_l_3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(spriteSheet[8]).convert_alpha(),(w + 30,h + 30)), False, True)
            self.groundpound_l_4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(spriteSheet[9]).convert_alpha(),(w + 30,h + 30)), False, True)
            self.groundpound_r_1 = self.groundpound_l_1
            self.groundpound_r_2 = self.groundpound_l_2
            self.groundpound_r_3 = self.groundpound_l_3
            self.groundpound_r_4 = self.groundpound_l_4

            self.roster = pygame.transform.scale(pygame.image.load(spriteSheet[22]).convert_alpha(),(100,100))
            self.rosterSelect = pygame.transform.scale(pygame.image.load(spriteSheet[24]).convert_alpha(),(212,212))

            self.sliding_l = pygame.transform.scale(pygame.image.load(spriteSheet[5]).convert_alpha(),(w,h))
            self.sliding_r = pygame.transform.flip(self.crouch_l, True, False)

            self.damaged_l = pygame.transform.scale(pygame.image.load(spriteSheet[23]).convert_alpha(),(w + 30,h + 30))
            self.damaged_r = pygame.transform.flip(self.damaged_l, True, False)

    #################### CHARACTER INFO ####################

    def __init__(self,name_arg,spriteSheet,location=[0,0],size=[50,50],uldr=[pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_e,pygame.K_q],hat=hats.none,weight=2,strength=10,speed=7):
        self.name = name_arg
        self.x = location[0]
        self.y = location[1]
        self.w = size[0]
        self.h = size[1]
        self.spriteSheet = spriteSheet
        self.sprites = self.spriteList(
            self.spriteSheet,
            self.w,
            self.h
        )
        self.sprite = self.sprites.idle_left
        self.uldr = uldr
        self.speed = speed*200*delta
        self.jumpVelocity = 0*80*delta
        self.horizontalVelocity = 0*200*delta
        self.facing = "left"
        self.runAnimFrame = 0
        self.dodgeAnimFrame = 0
        self.attackAnimFrame = 0
        self.weight = weight
        self.hat = hat
        self.hatAnimFrame = 1
        self.moving = False
        self.target = None
        self.deaths = 0
        self.kills = 0
        self.player = None
        self.damageFrame = 0
        self.health = 500
        self.spawn_point = (0,0)
        self.stock = 3
        self.strength = strength

    #################### PLAYER RENDER ####################

    def render(self): 
        if self.damageFrame > 0:
            self.sprite = pygame.transform.scale(self.sprites.damaged_l,(self.w * camera.scale,self.h * camera.scale))
            self.damageFrame -= 1
        if self.damageFrame <= 0:
            self.sprite =pygame.transform.scale(self.sprite,(self.w * camera.scale,self.h * camera.scale))
        window.blit(self.sprite,((self.x - camera.x) * camera.scale,(self.y - camera.y) * camera.scale))
        window.blit(pointer,(((self.x) - camera.x) * camera.scale,(((self.y - 50) - camera.y) * camera.scale)))
        if self.moving == False:
            if self.facing == "left":
                window.blit(self.hat,(((self.x) - camera.x) * camera.scale,((self.y - 20) - camera.y) * camera.scale))
            if self.facing == "right":
                window.blit(self.hat,((((self.x + self.w) - 20) - camera.x) * camera.scale,((self.y - 20) - camera.y) * camera.scale))
        if self.moving == True:
            if self.facing == "left":
                if self.hatAnimFrame in range(1,11):
                    window.blit(self.hat,(((self.x) - camera.x) * camera.scale,((self.y) - camera.y) * camera.scale))
                    self.hatAnimFrame += 1
                    return
                if self.hatAnimFrame in range(11,20):
                    window.blit(self.hat,(((self.x) - camera.x) * camera.scale,((self.y + 5) - camera.y) * camera.scale))
                    self.hatAnimFrame += 1
                    if self.hatAnimFrame == 19:
                        self.hatAnimFrame = 1
                    return

            if self.facing == "right":
                if self.hatAnimFrame in range(1,11):
                    window.blit(self.hat,((((self.x + self.w) - 20) - camera.x) * camera.scale,((self.y) - camera.y) * camera.scale))
                    self.hatAnimFrame += 1
                    return
                if self.hatAnimFrame in range(11,20):
                    window.blit(self.hat,((((self.x + self.w) - 20) - camera.x) * camera.scale,((self.y + 5) - camera.y) * camera.scale))
                    self.hatAnimFrame += 1
                    if self.hatAnimFrame == 19:
                        self.hatAnimFrame = 1
                    return
        
        #camera.x, camera.y = self.x - (width / 2), self.y - (height / 2)

    #################### PLAYER CONTROLLER ####################

    def controller(self):
        if self.offScreen() == True:
            self.target.character.kills += 1
            self.deaths += 1
            self.jumpVelocity = 0
            self.horizontalVelocity = 0
            self.health = 500
            self.x, self.y = self.spawn_point
            self.target.character.x, self.target.character.y = self.target.character.spawn_point
            camera.start_shake()
            self.stock -= 1
        if self.health <= 0:
            self.target.character.kills += 1
            self.deaths += 1
            self.jumpVelocity = 0
            self.horizontalVelocity = 0 
            self.health = 500
            self.x, self.y = self.spawn_point
            self.target.character.x, self.target.character.y = self.target.character.spawn_point
            camera.start_shake()
            self.stock -= 1
        
        #################### PLAYER CONTROLLER --> UP ####################

        if pygame.key.get_pressed()[self.uldr[0]]:
            
            if self.collidingGround():
                self.jumpVelocity = 20*80*delta
                window.blit(jump_ground,(((self.x - 5) - camera.x) * camera.scale,((self.y - 20) - camera.y) * camera.scale))  
            else:
                if self.facing == "left":
                    self.sprite = self.sprites.idle_left
                if self.facing == "right":
                    self.sprite = self.sprites.idle_right
            pass
            
            #################### PLAYER CONTROLLER --> UP --> IDLE ####################

        #################### PLAYER CONTROLLER --> LEFT ####################
        
        if pygame.key.get_pressed()[self.uldr[1]]:
            #beep.play()
            self.facing = "left"

            #################### PLAYER CONTROLLER --> LEFT --> ATTACK ####################
            
            if pygame.key.get_pressed()[self.uldr[4]]:
                
                if self.attackAnimFrame > 8:
                    self.attackAnimFrame = 1

                if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                    window.blit(self.sprites.side_l_1,(((self.x - 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_l_1
                    if (self.target.character.x < (self.x - 70) + 80 and
                        self.target.character.x + (self.target.character.w - 20) > (self.x - 70) and
                        self.target.character.y < (self.y - 30) + 80 and
                        self.target.character.y + self.target.character.h > (self.y - 30)):
                        self.target.character.horizontalVelocity -= (self.strength - self.target.character.weight)*60*delta
                        self.target.character.health -= 50
                        self.target.character.sprite = self.target.character.damageFrame = 10
                if self.attackAnimFrame == 3 or self.attackAnimFrame == 4:
                    window.blit(self.sprites.side_l_2,(((self.x - 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_l_2
                if self.attackAnimFrame == 5 or self.attackAnimFrame == 6:
                    window.blit(self.sprites.side_l_3,(((self.x - 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_l_3
                if self.attackAnimFrame == 7 or self.attackAnimFrame == 8:
                    window.blit(self.sprites.side_l_4,(((self.x - 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_l_4

                self.attackAnimFrame += 1
                return
            
            #################### PLAYER CONTROLLER --> LEFT --> DODGE ####################

            self.moving = True
            if pygame.key.get_pressed()[self.uldr[5]]:
                self.horizontalVelocity -= 2*60*delta
                if self.dodgeAnimFrame > 8:
                    self.dodgeAnimFrame = 1
                for i in range(5):
                    window.blit(bubble,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                else:
                    pass
                return
            
            #################### PLAYER CONTROLLER --> LEFT --> AIR ####################

            if self.collidingGround() == False:
                self.sprite = self.sprites.idle_left
                self.x -= self.speed
                return
            
            #################### PLAYER CONTROLLER --> LEFT --> CLIMBING ####################
            
            if self.collidingGround() == "right":
                self.y -= 2
                if pygame.key.get_pressed()[self.uldr[0]]:
                    self.x += 55
                    self.horizontalVelocity = -2*60*delta

                if self.runAnimFrame > 8:
                    self.runAnimFrame = 1

                if self.runAnimFrame == 1 or self.runAnimFrame == 2 or self.runAnimFrame == 3 or self.runAnimFrame == 4:
                    self.sprite = self.sprites.run_l_1
                if self.runAnimFrame == 5 or self.runAnimFrame == 6 or self.runAnimFrame == 7 or self.runAnimFrame == 8:
                    self.sprite = self.sprites.run_l_1
                self.runAnimFrame += 1
                return
            
            #################### PLAYER CONTROLLER --> LEFT --> RUNNING ####################

            if self.runAnimFrame > 8:
                self.runAnimFrame = 1

            if self.runAnimFrame == 1 or self.runAnimFrame == 2:
                self.sprite = self.sprites.run_l_1
            if self.runAnimFrame == 3 or self.runAnimFrame == 4:
                self.sprite = self.sprites.run_l_2
            if self.runAnimFrame == 5 or self.runAnimFrame == 6:
                self.sprite = self.sprites.run_l_3
            if self.runAnimFrame == 7 or self.runAnimFrame == 8:
                self.sprite = self.sprites.run_l_4
            self.runAnimFrame += 1
            self.x -= self.speed
            self.moving = True
            return
        
        #################### PLAYER CONTROLLER --> RIGHT ####################

        if pygame.key.get_pressed()[self.uldr[3]]:
            self.facing = "right"

            #################### PLAYER CONTROLLER --> RIGHT --> ATTACK ####################

            if pygame.key.get_pressed()[self.uldr[4]]:
                if self.attackAnimFrame > 8:
                    self.attackAnimFrame = 1

                if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                    window.blit(self.sprites.side_r_1,(((self.x + 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_r_1
                    if (self.target.character.x < (self.x + 70) + 80 and
                        self.target.character.x + (self.target.character.w - 20) > (self.x + 70) and
                        self.target.character.y < (self.y - 30) + 80 and
                        self.target.character.y + self.target.character.h > (self.y - 30)):
                        self.target.character.horizontalVelocity += (self.strength - self.target.character.weight)*60*delta
                        self.target.character.health -= 50
                        self.target.character.sprite = self.target.character.damageFrame = 10
                if self.attackAnimFrame == 3 or self.attackAnimFrame == 4:
                    window.blit(self.sprites.side_r_2,(((self.x + 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_r_2
                if self.attackAnimFrame == 5 or self.attackAnimFrame == 6:
                    window.blit(self.sprites.side_r_3,(((self.x + 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_r_3
                if self.attackAnimFrame == 7 or self.attackAnimFrame == 8:
                    window.blit(self.sprites.side_r_4,(((self.x + 70) - camera.x) * camera.scale,((self.y - 30) - camera.y) * camera.scale))
                    self.sprite = self.sprites.attacking_r_4

                self.attackAnimFrame += 1
                return
            
            #################### PLAYER CONTROLLER --> RIGHT --> DODGE ####################

            if pygame.key.get_pressed()[self.uldr[5]]:
                self.horizontalVelocity += 2*60*delta
                if self.dodgeAnimFrame > 8:
                    self.dodgeAnimFrame = 1

                for i in range(5):
                    window.blit(bubble,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                else:
                    pass
                return
            
            #################### PLAYER CONTROLLER --> RIGHT --> AIR ####################

            self.dodgeAnimFrame += 1
    
            if self.collidingGround() == False:
                self.sprite = self.sprites.idle_right
                self.x += self.speed
                return
            
            #################### PLAYER CONTROLLER --> RIGHT --> CLIMBING ####################
            
            if self.collidingGround() == "left":
                self.y -= 2
                if pygame.key.get_pressed()[self.uldr[0]]:
                    self.x -= 55
                return
            
            #################### PLAYER CONTROLLER --> RIGHT --> RUNNING ####################

            if self.runAnimFrame > 8:
                self.runAnimFrame = 1

            if self.runAnimFrame == 1 or self.runAnimFrame == 2:
                self.sprite = self.sprites.run_r_1
            if self.runAnimFrame == 3 or self.runAnimFrame == 4:
                self.sprite = self.sprites.run_r_2
            if self.runAnimFrame == 5 or self.runAnimFrame == 6:
                self.sprite = self.sprites.run_r_3
            if self.runAnimFrame == 7 or self.runAnimFrame == 8:
                self.sprite = self.sprites.run_r_4
            self.runAnimFrame += 1
            self.x += self.speed
            self.moving = True
            return
        
        #################### PLAYER CONTROLLER --> DOWN ####################
        
        if pygame.key.get_pressed()[self.uldr[2]]:

            #################### PLAYER CONTROLLER --> DOWN --> ATTACK ####################

            if pygame.key.get_pressed()[self.uldr[4]]:
                if self.collidingGround() == False:
                    self.y += self.speed * 2
                
                    if self.attackAnimFrame > 8:
                        self.attackAnimFrame = 1

                    if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                        window.blit(self.sprites.groundpound_l_1,(((self.x - 10) - camera.x) * camera.scale,((self.y + 70) - camera.y) * camera.scale))
                        self.sprite = self.sprites.attacking_l_1
                        if (self.target.character.x < (self.x - 70) + 80 and
                            self.target.character.x + (self.target.character.w - 20) > (self.x - 70) and
                            self.target.character.y < (self.y + 70) + 80 and
                            self.target.character.y + self.target.character.h > (self.y + 70)):
                            self.target.character.jumpVelocity += (self.strength - self.target.character.weight)*80*delta
                            self.target.character.health -= 50
                            self.target.character.sprite = self.target.character.damageFrame = 10
                    if self.attackAnimFrame == 3 or self.attackAnimFrame == 4:
                        window.blit(self.sprites.groundpound_l_2,(((self.x - 10) - camera.x) * camera.scale,((self.y + 70) - camera.y) * camera.scale))
                        self.sprite = self.sprites.attacking_l_2
                    if self.attackAnimFrame == 5 or self.attackAnimFrame == 6:
                        window.blit(self.sprites.groundpound_l_3,(((self.x - 10) - camera.x) * camera.scale,((self.y + 70) - camera.y) * camera.scale))
                        self.sprite = self.sprites.attacking_l_3
                    if self.attackAnimFrame == 7 or self.attackAnimFrame == 8:
                        window.blit(self.sprites.groundpound_l_4,(((self.x - 10) - camera.x) * camera.scale,((self.y + 70) - camera.y) * camera.scale))
                        self.sprite = self.sprites.attacking_l_4

                    self.attackAnimFrame += 1
                    return

            #################### PLAYER CONTROLLER --> DOWN --> AIR ####################    
            
            if self.collidingGround() == False:
                self.y += self.speed * 2
                if self.facing == "left": 
                    self.sprite = self.sprites.crouch_l
                if self.facing == "right":
                    self.sprite = self.sprites.crouch_r
                return
            else:
                if self.facing == "left": 
                    self.sprite = self.sprites.crouch_l
                if self.facing == "right":
                    self.sprite = self.sprites.crouch_r
                return

        #################### PLAYER CONTROLLER --> TESTING BUTTON ####################

        if pygame.key.get_pressed()[pygame.K_r]:
            self.horizontalVelocity = 1*60*delta

        #################### PLAYER CONTROLLER --> ATTACK ####################
        
        if pygame.key.get_pressed()[self.uldr[4]]:

            #################### PLAYER CONTROLLER --> ATTACK --> AIR ####################

            if self.collidingGround() == False:
                if pygame.key.get_pressed()[self.uldr[4]]:
                    if self.attackAnimFrame > 8:
                        self.attackAnimFrame = 1

                    #################### PLAYER CONTROLLER --> ATTACK --> AIR --> LEFT ####################

                    if self.facing == "left":
                        if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                            window.blit(self.sprites.spin_l_1,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_l_1
                            if (self.target.character.x < (self.x - 10) + 80 and
                                self.target.character.x + (self.target.character.w - 20) > (self.x - 10) and
                                self.target.character.y < (self.y - 10) + 80 and
                                self.target.character.y + self.target.character.h > (self.y - 10)):
                                self.target.character.horizontalVelocity -= (self.strength - self.target.character.weight)*60*delta
                                self.target.character.jumpVelocity -= (self.strength - self.target.character.weight)*80*delta
                                self.target.character.health -= 50
                                self.target.character.sprite = self.target.character.damageFrame = 10
                        if self.attackAnimFrame == 3 or self.attackAnimFrame == 4:
                            window.blit(self.sprites.spin_l_2,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_l_2
                        if self.attackAnimFrame == 5 or self.attackAnimFrame == 6:
                            window.blit(self.sprites.spin_l_3,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_l_3
                        if self.attackAnimFrame == 7 or self.attackAnimFrame == 8:
                            window.blit(self.sprites.spin_l_4,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_l_4

                    #################### PLAYER CONTROLLER --> ATTACK --> AIR --> RIGHT ####################

                    if self.facing == "right":
                        if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                            window.blit(self.sprites.spin_r_1,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_r_1
                            if (self.target.character.x < (self.x - 10) + 80 and
                                self.target.character.x + (self.target.character.w - 20) > (self.x - 10) and
                                self.target.character.y < (self.y - 10) + 80 and
                                self.target.character.y + self.target.character.h > (self.y - 10)):
                                self.target.character.horizontalVelocity += (self.strength - self.target.character.weight)*60*delta
                                self.target.character.jumpVelocity -= (self.strength - self.target.character.weight)*80*delta
                                self.target.character.health -= 50
                                self.target.character.sprite = self.target.character.damageFrame = 10
                        if self.attackAnimFrame == 3 or self.attackAnimFrame == 4:
                            window.blit(self.sprites.spin_r_2,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_r_2
                        if self.attackAnimFrame == 5 or self.attackAnimFrame == 6:
                            window.blit(self.sprites.spin_r_3,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_r_3
                        if self.attackAnimFrame == 7 or self.attackAnimFrame == 8:
                            window.blit(self.sprites.spin_r_4,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_r_4
                    self.attackAnimFrame += 1
                    return
            
            #################### PLAYER CONTROLLER --> ATTACK --> GROUNDED ####################
            
            if self.attackAnimFrame > 8:
                self.attackAnimFrame = 1

            #################### PLAYER CONTROLLER --> ATTACK --> FACING LEFT ####################

            if self.facing == "left":
                if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                    window.blit(self.sprites.attack_l_1,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))
                    if (self.target.character.x < (self.x - 10) + 80 and
                        self.target.character.x + (self.target.character.w - 20) > (self.x - 10) and
                        self.target.character.y < (self.y - 40) + 80 and
                        self.target.character.y + self.target.character.h > (self.y - 40)):
                        self.target.character.jumpVelocity += (self.strength - self.target.character.weight)*80*delta
                        self.target.character.health -= 50
                        self.target.character.sprite = self.target.character.damageFrame = 10
                if self.attackAnimFrame == 3 or self.attackAnimFrame == 4:
                    window.blit(self.sprites.attack_l_2,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))
                if self.attackAnimFrame == 5 or self.attackAnimFrame == 6:
                    window.blit(self.sprites.attack_l_3,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))
                if self.attackAnimFrame == 7 or self.attackAnimFrame == 8:
                    window.blit(self.sprites.attack_l_4,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))

            #################### PLAYER CONTROLLER --> ATTACK --> FACING RIGHT ####################

            if self.facing == "right":
                if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                    window.blit(self.sprites.attack_r_1,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))
                    if (self.target.character.x < (self.x - 10) + 80 and
                        self.target.character.x + (self.target.character.w - 20) > (self.x - 10) and
                        self.target.character.y < (self.y - 40) + 80 and
                        self.target.character.y + self.target.character.h > (self.y - 40)):
                        self.target.character.jumpVelocity += (self.strength - self.target.character.weight)*80*delta
                        self.target.character.health -= 50
                        self.target.character.sprite = self.target.character.damageFrame = 10
                if self.attackAnimFrame == 3 or self.attackAnimFrame == 4:
                    window.blit(self.sprites.attack_r_2,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))
                if self.attackAnimFrame == 5 or self.attackAnimFrame == 6:
                    window.blit(self.sprites.attack_r_3,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))
                if self.attackAnimFrame == 7 or self.attackAnimFrame == 8:
                    window.blit(self.sprites.attack_r_4,(((self.x - 10) - camera.x) * camera.scale,((self.y - 40) - camera.y) * camera.scale))
            self.attackAnimFrame += 1
            return
        
        #################### PLAYER CONTROLLER --> MIDDLE CLICK?????? ####################

        if pygame.mouse.get_pressed()[1]:
            pass

        #################### PLAYER CONTROLLER --> DODGE ####################

        if pygame.key.get_pressed()[self.uldr[5]]:
            if self.dodgeAnimFrame > 8:
                self.dodgeAnimFrame = 1

            #################### PLAYER CONTROLLER --> DODGE --> FACING LEFT ####################

            if self.facing == "left": 
                for i in range(5):
                    self.horizontalVelocity = 0*60*delta
                    self.jumpVelocity = 0
                    window.blit(bubble,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))

            #################### PLAYER CONTROLLER --> DODGE --> FACING RIGHT ####################

            if self.facing == "right":
                for i in range(5):
                    self.horizontalVelocity = 0*60*delta
                    self.jumpVelocity = 0
                    window.blit(bubble,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
            else:
                pass

            self.dodgeAnimFrame += 1
            return
        
        #################### PLAYER CONTROLLER --> DEFAULT (CONGRATUALATIONS YOU REACHED THE BOTTOM OF PLAYER>CONTROLLER()) ####################

        else:
            self.moving = False
            if self.facing == "left": 
                self.sprite = self.sprites.idle_left
            if self.facing == "right":
                self.sprite = self.sprites.idle_right
        
    #################### COLLIDING GROUND ####################
        
    def collidingGround(self):
        if ((self.x + 20) < stage.stage.x + stage.stage.w and
            self.x + (self.w - 20) > stage.stage.x and
            self.y < stage.stage.y + stage.stage.h and
            self.y + self.h > stage.stage.y):
            if self.y > stage.stage.y:
                if self.x <= stage.stage.x:
                    return "left"
                if self.x + (self.w) >= stage.stage.x + stage.stage.w:
                    return "right"
            else:
                return True
        else:
            return False
        
    #################### OFFSCREEN DEATH ####################

    def offScreen(self):
        if self.x > camera.x + pygame.display.Info().current_w or self.x + self.w < camera.x or self.y > camera.y + pygame.display.Info().current_h or self.y + self.h < camera.y:
            return True
        else:
            return False
        
    ####################

    def gravitate(self):

        #################### VELOCITY HANDLING ####################

        self.y -= self.jumpVelocity*80*delta
        self.x += self.horizontalVelocity*60*delta

        if self.horizontalVelocity > 0:
          self.horizontalVelocity -= 1*60*delta

        if self.horizontalVelocity < 0:
          self.horizontalVelocity += 1*60*delta

        if self.damageFrame > 0:
          self.damageFrame -= 1

        if self.damageFrame < 0:
          self.damageFrame += 1
        
        #################### CLIMBING ####################

        if self.collidingGround() == "left" or self.collidingGround() == "right":
            self.sprite = self.sprites.sliding_l
            self.jumpVelocity = -1*60*delta

        #################### GROUNDED ####################

        if self.collidingGround() == True:
            self.y = stage.stage.y - self.h
            self.jumpVelocity = 0

        #################### AIRBORNE ####################

        if self.collidingGround() == False:
            self.y += self.weight
            self.jumpVelocity -= 1*200*delta
        else:
            pass
        
#################### MICHAEL ####################
michael = character(
    name_arg="michael",
    spriteSheet=[
        f"{dir_path}/michael/idle_left.gif",
        f"{dir_path}/michael/run_left_1.gif",
        f"{dir_path}/michael/run_left_2.gif",
        f"{dir_path}/michael/run_left_3.gif",
        f"{dir_path}/michael/run_left_4.gif",
        f"{dir_path}/michael/crouch.gif",
        f"{dir_path}/michael/attack_anims/attack_1.gif",
        f"{dir_path}/michael/attack_anims/attack_2.gif",
        f"{dir_path}/michael/attack_anims/attack_3.gif",
        f"{dir_path}/michael/attack_anims/attack_4.gif",
        f"{dir_path}/michael/attack_anims/spin_1.gif",
        f"{dir_path}/michael/attack_anims/spin_2.gif",
        f"{dir_path}/michael/attack_anims/spin_3.gif",
        f"{dir_path}/michael/attack_anims/spin_4.gif",
        f"{dir_path}/michael/attack_anims/side_1.gif",
        f"{dir_path}/michael/attack_anims/side_2.gif",
        f"{dir_path}/michael/attack_anims/side_3.gif",
        f"{dir_path}/michael/attack_anims/side_4.gif",
        f"{dir_path}/michael/attacking_1.gif",
        f"{dir_path}/michael/attacking_2.gif",
        f"{dir_path}/michael/attacking_3.gif",
        f"{dir_path}/michael/attacking_4.gif",
        f"{dir_path}/michael/roster.gif",
        f"{dir_path}/michael/damaged.gif",
        f"{dir_path}/michael/roster2.gif",
    ],
    location=[stage.stage.x + 100,stage.stage.y - 100],
    #uldr=[pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g],
    weight=2,
    strength=10,
    speed=7,
)

#################### BELL ####################

bell = character(
    name_arg="bell",
    spriteSheet=[
        f"{dir_path}/bell/idle_left.gif",
        f"{dir_path}/bell/run_left_1.gif",
        f"{dir_path}/bell/run_left_2.gif",
        f"{dir_path}/bell/run_left_3.gif",
        f"{dir_path}/bell/run_left_4.gif",
        f"{dir_path}/bell/crouch.gif",
        f"{dir_path}/bell/attack_anims/attack_1.gif",
        f"{dir_path}/bell/attack_anims/attack_2.gif",
        f"{dir_path}/bell/attack_anims/attack_3.gif",
        f"{dir_path}/bell/attack_anims/attack_4.gif",
        f"{dir_path}/bell/attack_anims/spin_1.gif",
        f"{dir_path}/bell/attack_anims/spin_2.gif",
        f"{dir_path}/bell/attack_anims/spin_3.gif",
        f"{dir_path}/bell/attack_anims/spin_4.gif",
        f"{dir_path}/bell/attack_anims/side_1.gif",
        f"{dir_path}/bell/attack_anims/side_2.gif",
        f"{dir_path}/bell/attack_anims/side_3.gif",
        f"{dir_path}/bell/attack_anims/side_4.gif",
        f"{dir_path}/bell/attacking_1.gif",
        f"{dir_path}/bell/attacking_2.gif",
        f"{dir_path}/bell/attacking_3.gif",
        f"{dir_path}/bell/attacking_4.gif",
        f"{dir_path}/bell/roster.gif",
        f"{dir_path}/bell/damaged.gif",
        f"{dir_path}/bell/roster2.gif",
    ],
    location=[stage.stage.x + 100,stage.stage.y - 100],
    #uldr=[pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL],
    weight=2,
    strength=10,
    speed=9,
)

gus = character(
    name_arg="gus",
    spriteSheet=[
        f"{dir_path}/gus/idle_left.gif",
        f"{dir_path}/gus/run_left_1.gif",
        f"{dir_path}/gus/run_left_2.gif",
        f"{dir_path}/gus/run_left_3.gif",
        f"{dir_path}/gus/run_left_4.gif",
        f"{dir_path}/gus/crouch.gif",
        f"{dir_path}/gus/attack_anims/attack_1.gif",
        f"{dir_path}/gus/attack_anims/attack_2.gif",
        f"{dir_path}/gus/attack_anims/attack_3.gif",
        f"{dir_path}/gus/attack_anims/attack_4.gif",
        f"{dir_path}/gus/attack_anims/spin_1.gif",
        f"{dir_path}/gus/attack_anims/spin_2.gif",
        f"{dir_path}/gus/attack_anims/spin_3.gif",
        f"{dir_path}/gus/attack_anims/spin_4.gif",
        f"{dir_path}/gus/attack_anims/side_1.gif",
        f"{dir_path}/gus/attack_anims/side_2.gif",
        f"{dir_path}/gus/attack_anims/side_3.gif",
        f"{dir_path}/gus/attack_anims/side_4.gif",
        f"{dir_path}/gus/attacking_1.gif",
        f"{dir_path}/gus/attacking_2.gif",
        f"{dir_path}/gus/attacking_3.gif",
        f"{dir_path}/gus/attacking_4.gif",
        f"{dir_path}/gus/roster.gif",
        f"{dir_path}/gus/damaged.gif",
        f"{dir_path}/gus/roster2.gif",
    ],
    location=[stage.stage.x + 100,stage.stage.y - 100],
    #uldr=[pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL],
    weight=2,
    hat=hats.cowboy,
    strength=13,
    speed=6,
)

draedon = character(
    name_arg="draedon",
    spriteSheet=[
        f"{dir_path}/draedon/idle_left.gif",
        f"{dir_path}/draedon/run_left_1.gif",
        f"{dir_path}/draedon/run_left_2.gif",
        f"{dir_path}/draedon/run_left_3.gif",
        f"{dir_path}/draedon/run_left_4.gif",
        f"{dir_path}/draedon/crouch.gif",
        f"{dir_path}/draedon/attack_anims/attack_1.gif",
        f"{dir_path}/draedon/attack_anims/attack_2.gif",
        f"{dir_path}/draedon/attack_anims/attack_3.gif",
        f"{dir_path}/draedon/attack_anims/attack_4.gif",
        f"{dir_path}/draedon/attack_anims/spin_1.gif",
        f"{dir_path}/draedon/attack_anims/spin_2.gif",
        f"{dir_path}/draedon/attack_anims/spin_3.gif",
        f"{dir_path}/draedon/attack_anims/spin_4.gif",
        f"{dir_path}/draedon/attack_anims/side_1.gif",
        f"{dir_path}/draedon/attack_anims/side_2.gif",
        f"{dir_path}/draedon/attack_anims/side_3.gif",
        f"{dir_path}/draedon/attack_anims/side_4.gif",
        f"{dir_path}/draedon/attacking_1.gif",
        f"{dir_path}/draedon/attacking_2.gif",
        f"{dir_path}/draedon/attacking_3.gif",
        f"{dir_path}/draedon/attacking_4.gif",
        f"{dir_path}/draedon/roster.gif",
        f"{dir_path}/draedon/damaged.gif",
        f"{dir_path}/draedon/roster2.gif",
    ],
    location=[stage.stage.x + 100,stage.stage.y - 100],
    #uldr=[pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL],
    weight=2,
    hat=hats.tophat,
    strength=15,
    speed=5,
)

dante = character(
    name_arg="dante",
    spriteSheet=[
        f"{dir_path}/dante/idle_left.gif",
        f"{dir_path}/dante/run_left_1.gif",
        f"{dir_path}/dante/run_left_2.gif",
        f"{dir_path}/dante/run_left_3.gif",
        f"{dir_path}/dante/run_left_4.gif",
        f"{dir_path}/dante/crouch.gif",
        f"{dir_path}/dante/attack_anims/attack_1.gif",
        f"{dir_path}/dante/attack_anims/attack_2.gif",
        f"{dir_path}/dante/attack_anims/attack_3.gif",
        f"{dir_path}/dante/attack_anims/attack_4.gif",
        f"{dir_path}/dante/attack_anims/spin_1.gif",
        f"{dir_path}/dante/attack_anims/spin_2.gif",
        f"{dir_path}/dante/attack_anims/spin_3.gif",
        f"{dir_path}/dante/attack_anims/spin_4.gif",
        f"{dir_path}/dante/attack_anims/side_1.gif",
        f"{dir_path}/dante/attack_anims/side_2.gif",
        f"{dir_path}/dante/attack_anims/side_3.gif",
        f"{dir_path}/dante/attack_anims/side_4.gif",
        f"{dir_path}/dante/attacking_1.gif",
        f"{dir_path}/dante/attacking_2.gif",
        f"{dir_path}/dante/attacking_3.gif",
        f"{dir_path}/dante/attacking_4.gif",
        f"{dir_path}/dante/roster.gif",
        f"{dir_path}/dante/damaged.gif",
        f"{dir_path}/dante/roster2.gif",
    ],
    location=[stage.stage.x + 100,stage.stage.y - 100],
    #uldr=[pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL],
    weight=3,
    hat=hats.none,
    strength=20,
    speed=3,
)

no_char = character(
    name_arg="",
    spriteSheet=[
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
        f"{dir_path}/none_hat.gif",
    ],
    location=[stage.stage.x + 100,stage.stage.y - 100],
    #uldr=[pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL],
    weight=0,
    hat=hats.none,
    strength=0,
    speed=0,
)

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
            self.character.spawn_point = (stage.stage.x, stage.stage.y - 100)
            self.character.x, self.character.y = self.character.spawn_point
        if self.name == "player2":
            self.character.spawn_point = (stage.stage.x + (stage.stage.w - self.character.w), stage.stage.y - 100)
            self.character.x, self.character.y = self.character.spawn_point
    def handleCharacter(self):
        self.character.render()
        self.character.controller()
        self.character.gravitate()
        if self.name == "player1":
            play = text(size=36, text=f"{self.character.name} ({self.name})")
            play.render(10,110)
            window.blit(self.character.sprites.roster, (10,10))
        if self.name == "player2":            
            play = text(size=36, text=f"{self.character.name} ({self.name})")
            play.render(pygame.display.Info().current_w - play.text.get_width(),110)
            window.blit(self.character.sprites.roster, (pygame.display.Info().current_w - 110,10))

#################### PLAYERS 1 & 2 ####################

player1 = player([pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g],"player1")
player2 = player([pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL],"player2")

player1.target = player2
player2.target = player1

#################### SET CHARACTERS ####################

#################### TEXT ##############################

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

