import pygame
from random import randrange
from apple2 import Apple# class Apple

Window = 800# Size
x, y = randrange(100, Window-100), randrange(100, Window-100)# cords of snake
bg = pygame.image.load('1.jpg') # background image
score = 0
lenght =1
snake = [(x,y)]
dx, dy =0, 0#default direction
fps = 60
speed= 6# beginning speed
sc = pygame.display.set_mode([Window,Window])
clock = pygame.time.Clock()
apple= Apple(randrange(100, Window-100),randrange(100, Window-100),sc)# Apple