import pygame
#function of snakes control
def control(dx,dy,key):
    if key[pygame.K_UP]:
       dx, dy= 0,-1
    if key[pygame.K_DOWN]:
        dx, dy = 0, 1   
    if key[pygame.K_LEFT]:
       dx, dy = -1, 0
    if key[pygame.K_RIGHT]:
        dx, dy = 1, 0    
    return dx, dy # direction   