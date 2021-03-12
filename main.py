import pygame
from random import randrange
from bones2 import Bones
from control import control
from game_over import game_over
from eating import eating
from variables import * 
from score import scored

pygame.init()

while True:
    sc.blit(bg,(0,0)) #background
    [(pygame.draw.rect(sc, 'purple',(n,m,50,50)))for n,m in snake]#snake
    x+=dx * speed
    y+=dy * speed# moves of snake
    snake.append((x,y)) 
    snake = snake[-lenght:]#length adjustment
    apple.draw() #apple

    lenght,speed,score,apple.paddle.x,apple.paddle.y = eating(apple.paddle.x,x,apple.paddle.y,y,lenght,speed,score)# function eating (apple)
    game_over(x,y,len(snake),len(set(snake)),sc)# function game over
    scored(score,sc)# function score
    key = pygame.key.get_pressed()
    dx, dy=control(dx,dy,key)# control of snake function

    for i in range(1,len(snake)-1,5):
        b= Bones(sc)
        b.draw(snake[i][0],snake[i][1])# drawing bones of snake
             
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit() 

    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)
   