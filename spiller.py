from figur import Figur

class Spiller(Figur):
    def __init__(self, x: int, y: int, bredde: int, hoyde: int):
        super().__init__(x, y, bredde, hoyde)
        self.speed = 0
        self.score = 0
     
        
    def animation(self):
        self.ramme.y += self.speed
        if self.ramme.top <= 0:
            self.ramme.top = 0
        if self.ramme.bottom >= 750:
            self.ramme.bottom = 750