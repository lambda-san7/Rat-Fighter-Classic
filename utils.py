import pygame
import os 

pygame.init()

dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.display.set_caption("Template")

#pygame.display.set_icon(favicon)

########################
# SPRITES
########################

#favicon = pygame.image.load(f"{dir_path}/*insert name*.png")
#sprite = pygame.transform.scale(pygame.image.load(f"{dir_path}/*insert name*.png"),(200,200))

class favicon:
    def __init__(self,file_name="mySprite.png"):
        self.sprite = pygame.image.load(f"{dir_path}/{file_name}")

class sprite:
    def __init__(self,file_name="mySprite.png",w=100,h=100):
        self.sprite = pygame.transform.scale(pygame.image.load(f"{dir_path}/{file_name}"),(w,h))
    def render(self,x,y):
        window.blit(self.sprite,(x,y))

########################
# UTILS
########################

def create_window(w=1000,h=500,title="Blank",favicon="favicon.png"):
    window = pygame.display.set_mode((w,h),pygame.RESIZABLE)
    pygame.display.set_caption(title)
    #pygame.display.set_icon(favicon)
    return window

window = create_window(w=900,h=600,title="Utilities")


class center:
    def x(w):
        return (pygame.display.Info().current_w / 2) - (w / 2)
    def y(h):
        return (pygame.display.Info().current_h / 2) - (h / 2)

class button:
    def __init__(self,txt,size,color):
        self.color = color
        self.txt = text(size,str(txt),self.color,thicc=2)
    def render(self,x,y):
        self.txt.render(x,y)
    def hover(self,x,y):
        return (pygame.mouse.get_pos()[0] < x + self.txt.w and
            pygame.mouse.get_pos()[0] > x and
            pygame.mouse.get_pos()[1] < y + self.txt.h and
            pygame.mouse.get_pos()[1] > y)
    def click(self,x,y):
        if (pygame.mouse.get_pos()[0] < x + self.txt.w and
            pygame.mouse.get_pos()[0] > x and
            pygame.mouse.get_pos()[1] < y + self.txt.h and
            pygame.mouse.get_pos()[1] > y):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        else:
            return False

class text:
    def __init__(self, size, text, color=(255,255,255),thicc=0,color2=(0,0,0),font_file="font.ttf"):
        self.font = pygame.font.Font(f"{dir_path}/{font_file}",size)
        self.color = color
        self.text_holder = text
        self.font_holder = font_file
        self.size_holder = size
        self.border_thickness = thicc
        self.border_color = color2
        self.text = self.font.render(text, True, self.color)
        self.w = self.text.get_width()
        self.h = self.text.get_height()
    def render(self,x,y):
        self.font = pygame.font.Font(f"{dir_path}/{self.font_holder}",self.size_holder)
        self.text = self.font.render(self.text_holder, True, self.border_color)
        window.blit(self.text,(x,y - self.border_thickness))
        window.blit(self.text,(x,y + self.border_thickness))
        window.blit(self.text,(x - self.border_thickness,y))
        window.blit(self.text,(x + self.border_thickness,y))
        self.text = self.font.render(self.text_holder, True, self.color)
        window.blit(self.text,(x,y))

class input:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.active = False
        self.content = ""
    def render(self,x,y):
        pygame.draw.rect(window,(0,0,0),(x,y,self.w,self.h))
        msg = text(32,self.content,thicc=2)
        msg.render(x,y)
    def click(self,x,y):
        if (pygame.mouse.get_pos()[0] < x + self.w and
            pygame.mouse.get_pos()[0] > x and
            pygame.mouse.get_pos()[1] < y + self.h and
            pygame.mouse.get_pos()[1] > y):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.active = True
                    print("active")
                    return True
        else:
            self.active = False
            return False
        
    def typing(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    letter = chr(event.key)
                    self.content += letter
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key)
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:  # Check if SHIFT key is pressed
                        letter = letter.upper()
                    else:
                        letter = letter.lower()
                    self.content += letter
                if event.key == pygame.K_BACKSPACE:
                    letter = chr(event.key)
                    modified_title = self.content[:-1]
                    self.content = modified_title