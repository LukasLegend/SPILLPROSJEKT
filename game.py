import pygame
from ball import Ball




def spiller_animation():
    spiller.y += spiller_speed
    if spiller.top <= 0:
        spiller.top = 0
    if spiller.bottom >= HOYDE:
        spiller.bottom = HOYDE

def motstander_animation():
    if motstander.top < ball.ramme.y:
        motstander.top += motstander_speed
    if motstander.bottom > ball.ramme.y:
        motstander.bottom -= motstander_speed
    if motstander.top <= 0:
        motstander.top = 0
    if motstander.bottom >= HOYDE:
        motstander.bottom = HOYDE



pygame.init()

BREDDE = 1280
HOYDE = 750
FPS = 60

ball = Ball(BREDDE/2 -15, HOYDE/2 -15, 30, 30)


vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()





spiller = pygame.Rect (BREDDE - 20, HOYDE/2 -70, 10, 140)
spiller_speed = 0

motstander = pygame.Rect(10, HOYDE/2 -70, 10, 140)
motstander_speed = 15

spiller_score = 0
motstander_score = 0
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
                spiller_speed += 7
            if event.key == pygame.K_UP:
                spiller_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                spiller_speed -= 7
            if event.key == pygame.K_UP:
                spiller_speed += 7
    
    ball.animation()
    spiller_animation()
    motstander_animation()

    if ball.ramme.x <= 0:
        spiller_score += 1
        ball.restart()

    if ball.ramme.x >= BREDDE:
        motstander_score += 1
        ball.restart()

    if ball.ramme.colliderect(spiller) or ball.ramme.colliderect(motstander):
        ball.speed_x *= -1
        
    vindu.fill(bakgrunnsfarge)       
    pygame.draw.rect(vindu, light_grey, spiller)
    pygame.draw.rect(vindu, light_grey, motstander)
    
    pygame.draw.ellipse(vindu, light_grey, ball.ramme)
    pygame.draw.aaline(vindu, light_grey, (BREDDE/2,0), (BREDDE/2, HOYDE))
        
    spiller_text = game_font.render(f"{spiller_score}", False, light_grey)
    vindu.blit(spiller_text, (660, 400))

    motstander_text = game_font.render(f"{motstander_score}", False, light_grey)
    vindu.blit(motstander_text, (600, 400))

    
    pygame.display.flip()
    klokke.tick(FPS)
