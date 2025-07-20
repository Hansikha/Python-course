import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
caption = pygame.display.set_caption("MY FRIST GAME SCREEN")
DONE = False

while not DONE:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      DONE = True
screen.fill((255,255,255))
pygame.draw.rect(screen, (227,115,131), pygame.Rect(30, 30, 60, 60), 0)

pygame.display.flip()
