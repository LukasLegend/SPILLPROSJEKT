from figur import Figur
import random

class Ball(Figur):
    def __init__(self, x: int, y: int, bredde: int, hoyde: int):
        super().__init__(x, y, bredde, hoyde)
        self.ramme.centerx = bredde
        self.ramme.centery = hoyde
        self.speed_x = 15 * random.choice((1, -1))
        self.speed_y = 15 * random.choice((1, -1))


    def restart(self):
        self.ramme.center = (1280/2, 750/2)
        self.speed_y *= random.choice((1, -1))
        self.speed_x *= random.choice((1, -1))


    def animation(self):
        self.ramme.x += self.speed_x
        self.ramme.y += self.speed_y

        if self.ramme.top <= 0 or self.ramme.bottom >= 750:
            self.speed_y *= -1



