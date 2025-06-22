import pygame
pygame.init()
canvas = pygame.display.set_mode((500,500))
canvas.fill((255,255,255))
PINK = (255, 192, 203)
GREEN = (0, 255, 0)
done = False
while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    pygame.draw.circle(canvas, PINK, (200,200), 50, 0)
    pygame.draw.circle(canvas, GREEN, (400, 400), 50, 3)
    pygame.display.flip()
