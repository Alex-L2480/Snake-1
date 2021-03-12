import pygame
#function of output score to the screen
def scored(score,sc):
    font = pygame.font.SysFont('Tahoma', 26)
    render_score = font.render(f'SCORE:{score}',1,pygame.Color('white'))# f-string - changing score
    sc.blit(render_score,(5,5))