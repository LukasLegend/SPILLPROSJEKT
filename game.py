import pygame

pygame.init()

BREDDE = 1280
HOYDE = 960
FPS = 60

vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
pygame.display.flip()
clock.tick(FPS)





