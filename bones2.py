import pygame

img1 = pygame.image.load('2.png')
img1.set_colorkey('black')
img1.set_alpha(50)
#Bones class
class Bones:
    def __init__(self,surf):
        self.surf = surf
        self.image = img1
    def draw(self,x,y):
        self.x=x
        self.y=y
        self.surf.blit(self.image,(self.x,self.y))
        