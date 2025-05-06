import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
caption = pygame.display.set_caption("MY FRIST GAME SCREEN")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(200,155,207),pygame.Rect(200, 250, 100, 50),0)
    pygame.display.flip()
    pygame.draw.rect(screen,(200,155,207),pygame.Rect(200, 250, 100, 50),0)
    color = (58, 58, 58)
 
    screen.fill(color)
    pygame.display.flip()
    

    
    







     



