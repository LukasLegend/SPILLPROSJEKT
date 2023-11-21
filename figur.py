import pygame

class Figur:
    def __init__(self, x: int, y: int, bredde: int, hoyde: int):
        self.x = x
        self.y = y
        self.bredde = bredde
        self.hoyde = hoyde
        self.ramme = pygame.rect.Rect(x, y, bredde, hoyde)

    


    
    