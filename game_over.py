import pygame
import time

# game over conditions
#v = len(snake)
#z = len(set(snake))
def game_over(x,y,v,z,sc):
    if x>755 or x<-5 or y>755 or y<-5 or v != z:
        font1 = pygame.font.SysFont('Tahoma', 50)
        game_over = font1.render('GAME OVER',1,pygame.Color('black'))#forming the label
        sc.blit(game_over,(270,350))
        pygame.display.flip()
        time.sleep(1.5)# delay
        quit()    





