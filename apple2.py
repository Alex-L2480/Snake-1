import pygame
from random import randrange
img = pygame.image.load('3.png')
img.set_colorkey('white')
# Apple class
class Apple:
    def __init__(self,x,y,surf):
        self.x=x
        self.y=y
        self.surf = surf
        self.image = img
        self.paddle = self.image.get_rect(bottomleft=(self.x,self.y))
    def draw(self):
        self.surf.blit(self.image,self.paddle)
     
