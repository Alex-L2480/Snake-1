import pygame
from random import randrange
#eating apple function
def eating(applex,x,appley,y,lenght,speed,score):
    if applex-40<x<applex+40 and appley-50<y<appley+50:
        lenght+=5 # increasing
        speed+=0.2
        score+=100
        applex= (randrange(0,750))#new apple cords
        appley=(randrange(0,750))
    return lenght,speed,score,applex,appley 