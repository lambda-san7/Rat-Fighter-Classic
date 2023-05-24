import pygame
from camera import camera
from window import window
from window import width, height
from default import gravityAffected
from map import stage 

bubble = pygame.transform.scale(pygame.image.load("bubble.gif").convert_alpha(),(60,60))

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

    #################### CHARACTER INFO ####################

    def __init__(self,spriteSheet,location=[0,0],size=[50,50],uldr=[pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_e,pygame.K_q]):
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
        self.speed = 10
        self.jumpVelocity = 0
        self.facing = "left"
        self.jumps = 3
        self.runAnimFrame = 0
        self.dodgeAnimFrame = 0
        self.attackAnimFrame = 0

    #################### PLAYER RENDER ####################

    def render(self): 
        self.sprite = pygame.transform.scale(self.sprite,(self.w * camera.scale,self.h * camera.scale))
        window.blit(self.sprite,((self.x - camera.x) * camera.scale,(self.y - camera.y) * camera.scale))
        #camera.x, camera.y = self.x - (width / 2), self.y - (height / 2)

    #################### PLAYER CONTROLLER ####################

    def controller(self):
        if self.offScreen() == True:
            self.x, self.y = stage.x + 100,stage.y - 100
        
        #################### PLAYER CONTROLLER --> UP ####################

        if pygame.key.get_pressed()[self.uldr[0]]:

            #################### PLAYER CONTROLLER --> UP --> IDLE ####################

            if self.jumps != 0:
                self.jumpVelocity = 25
                self.jumps -= 1
            else:
                if self.facing == "left":
                    self.sprite = self.sprites.idle_left
                if self.facing == "right":
                    self.sprite = self.sprites.idle_right
                pass

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

            self.x -= self.speed
            if pygame.key.get_pressed()[self.uldr[5]]:
                self.x += 1
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
                self.x -= 5
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

            self.x += self.speed
            if pygame.key.get_pressed()[self.uldr[5]]:
                self.x -= 1
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
                self.x += 5
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

        #################### PLAYER CONTROLLER --> RESTART BUTTON IS STILL IN THE GAME PLEASE REMOVE THIS!!!! ####################    

        if pygame.key.get_pressed()[pygame.K_r]:
            self.x = 100 
            self.y = 0

        #################### PLAYER CONTROLLER --> ATTACK ####################
        
        if pygame.key.get_pressed()[self.uldr[4]]:

            #################### PLAYER CONTROLLER --> ATTACK --> AIR ####################

            if self.collidingGround() == False:
                if pygame.key.get_pressed()[self.uldr[4]]:
                    if self.attackAnimFrame > 8:
                        self.attackAnimFrame = 1

                    #################### PLAYER CONTROLLER --> ATTACK --> AIR --> LEFT ####################

                    if self.facing == "left":
                        print("left")
                        if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                            window.blit(self.sprites.spin_l_1,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_l_1
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
                        print("right")
                        if self.attackAnimFrame == 1 or self.attackAnimFrame == 2:
                            window.blit(self.sprites.spin_r_1,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
                            self.sprite = self.sprites.attacking_r_1
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
                    window.blit(bubble,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))

            #################### PLAYER CONTROLLER --> DODGE --> FACING RIGHT ####################

            if self.facing == "right":
                for i in range(5):
                    window.blit(bubble,(((self.x - 10) - camera.x) * camera.scale,((self.y - 10) - camera.y) * camera.scale))
            else:
                pass

            self.dodgeAnimFrame += 1
            return
        
        #################### PLAYER CONTROLLER --> DEFAULT (CONGRATUALATIONS YOU REACHED THE BOTTOM OF PLAYER>CONTROLLER()) ####################

        else:
            if self.facing == "left": 
                self.sprite = self.sprites.idle_left
            if self.facing == "right":
                self.sprite = self.sprites.idle_right
        
    #################### COLLIDING GROUND ####################
        
    def collidingGround(self):
        if (self.x + 20) < stage.x + stage.w and self.x + (self.w - 20) > stage.x and self.y < stage.y + stage.h and self.y + self.h > stage.y:
            return True
        else:
            return False
        
    #################### OFFSCREEN DEATH ####################

    def offScreen(self):
        if self.x > camera.x + width or self.x + self.w < camera.x or self.y > camera.y + height or self.y + self.h < camera.y:
            self.jumps = 3
            return True
        else:
            return False
        
#################### MICHAEL ####################

michael = character(
    spriteSheet=[
        "michael/idle_left.gif",
        "michael/run_left_1.gif",
        "michael/run_left_2.gif",
        "michael/run_left_3.gif",
        "michael/run_left_4.gif",
        "michael/crouch.gif",
        "michael/attack_anims/attack_1.gif",
        "michael/attack_anims/attack_2.gif",
        "michael/attack_anims/attack_3.gif",
        "michael/attack_anims/attack_4.gif",
        "michael/attack_anims/spin_1.gif",
        "michael/attack_anims/spin_2.gif",
        "michael/attack_anims/spin_3.gif",
        "michael/attack_anims/spin_4.gif",
        "michael/attack_anims/side_1.gif",
        "michael/attack_anims/side_2.gif",
        "michael/attack_anims/side_3.gif",
        "michael/attack_anims/side_4.gif",
        "michael/attacking_1.gif",
        "michael/attacking_2.gif",
        "michael/attacking_3.gif",
        "michael/attacking_4.gif",
    ],
    location=[stage.x + 100,stage.y - 100],
    uldr=[pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g]
)

gravityAffected.append(michael)

#################### BELL ####################

bell = character(
    spriteSheet=[
        "bell/idle_left.gif",
        "bell/run_left_1.gif",
        "bell/run_left_2.gif",
        "bell/run_left_3.gif",
        "bell/run_left_4.gif",
        "bell/crouch.gif",
        "bell/attack_anims/attack_1.gif",
        "bell/attack_anims/attack_2.gif",
        "bell/attack_anims/attack_3.gif",
        "bell/attack_anims/attack_4.gif",
        "bell/attack_anims/spin_1.gif",
        "bell/attack_anims/spin_2.gif",
        "bell/attack_anims/spin_3.gif",
        "bell/attack_anims/spin_4.gif",
        "bell/attack_anims/side_1.gif",
        "bell/attack_anims/side_2.gif",
        "bell/attack_anims/side_3.gif",
        "bell/attack_anims/side_4.gif",
        "michael/attacking_1.gif",
        "michael/attacking_2.gif",
        "michael/attacking_3.gif",
        "michael/attacking_4.gif",
    ],
    location=[stage.x + 100,stage.y - 100],
    uldr=[pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_RALT,pygame.K_RCTRL]
)

gravityAffected.append(bell)