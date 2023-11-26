import pygame
from ball import Ball
from spiller import Spiller
from motstander import Motstander

pygame.init()

BREDDE = 1280
HOYDE = 750
FPS = 60

ball = Ball(BREDDE/2 - 15, HOYDE/2 - 15, 30, 30)
spiller = Spiller(BREDDE - 10, HOYDE/2 - 70, 10, 140)
motstander = Motstander(10, HOYDE/2 - 70, 10, 140)

vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

game_font = pygame.font.Font("freesansbold.ttf", 32)

bakgrunnsfarge = pygame.Color('grey12')
light_grey = (200, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                spiller.speed += 7
            if event.key == pygame.K_UP:
                spiller.speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                spiller.speed -= 7
            if event.key == pygame.K_UP:
                spiller.speed += 7
    
    ball.animation()
    spiller.animation()

    if ball.ramme.x <= 0:
        spiller.score += 1
        ball.restart()

    if ball.ramme.x >= BREDDE:
        motstander.score += 1
        ball.restart()

    if ball.ramme.colliderect(spiller.ramme) or ball.ramme.colliderect(motstander.ramme):
        ball.speed_x *= -1

    if motstander.ramme.top < ball.ramme.y:
        motstander.ramme.top += motstander.speed

    if motstander.ramme.bottom > ball.ramme.y:
        motstander.ramme.bottom -= motstander.speed

    if motstander.ramme.top <= 0:
        motstander.ramme.top = 0

    if motstander.ramme.bottom >= HOYDE:
        motstander.ramme.bottom = HOYDE

        
    vindu.fill(bakgrunnsfarge)       
    pygame.draw.rect(vindu, light_grey, spiller.ramme)
    pygame.draw.rect(vindu, light_grey, motstander.ramme)
    
    pygame.draw.ellipse(vindu, light_grey, ball.ramme)
    pygame.draw.aaline(vindu, light_grey, (BREDDE/2,0), (BREDDE/2, HOYDE))
        
    spiller_text = game_font.render(f"{spiller.score}", False, light_grey)
    vindu.blit(spiller_text, (660, 400))
    
    motstander_text = game_font.render(f"{motstander.score}", False, light_grey)
    vindu.blit(motstander_text, (600, 400))

    
    pygame.display.flip()
    klokke.tick(FPS)
