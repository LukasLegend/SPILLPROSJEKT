import pygame, random

def ball_animation():
    global ball_speed_x, ball_speed_y, spiller_score, motstander_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HOYDE:
        ball_speed_y *= -1

    if ball.left <= 0:
        spiller_score += 1
        ball_restart()

    if ball.right >= BREDDE:
        motstander_score += 1
        ball_restart()

    if ball.colliderect(spiller) or ball.colliderect(motstander):
        ball_speed_x *= -1

def spiller_animation():
    spiller.y += spiller_speed
    if spiller.top <= 0:
        spiller.top = 0
    if spiller.bottom >= HOYDE:
        spiller.bottom = HOYDE

def motstander_animation():
    if motstander.top < ball.y:
        motstander.top += motstander_speed
    if motstander.bottom > ball.y:
        motstander.bottom -= motstander_speed
    if motstander.top <= 0:
        motstander.top = 0
    if motstander.bottom >= HOYDE:
        motstander.bottom = HOYDE

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (BREDDE/2, HOYDE/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

pygame.init()

BREDDE = 1280
HOYDE = 750
FPS = 60


vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

ball = pygame.Rect(BREDDE/2 - 15, HOYDE/2 - 15, 30, 30)
ball_speed_x = 15 * random.choice((1, -1))
ball_speed_y = 15 * random.choice((1, -1))

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
    
    ball_animation()
    spiller_animation()
    motstander_animation()
        
    vindu.fill(bakgrunnsfarge)       
    pygame.draw.rect(vindu, light_grey, spiller)
    pygame.draw.rect(vindu, light_grey, motstander)
    pygame.draw.ellipse(vindu, light_grey, ball)
    pygame.draw.aaline(vindu, light_grey, (BREDDE/2,0), (BREDDE/2, HOYDE))
        
    spiller_text = game_font.render(f"{spiller_score}", False, light_grey)
    vindu.blit(spiller_text, (660, 400))

    motstander_text = game_font.render(f"{motstander_score}", False, light_grey)
    vindu.blit(motstander_text, (600, 400))

    

    pygame.display.flip()
    klokke.tick(FPS)
