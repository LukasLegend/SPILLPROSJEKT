from figur import Figur

class Motstander(Figur):
    def __init__(self, x: int, y: int, bredde: int, hoyde: int):
        super().__init__(x, y, bredde, hoyde)
        self.speed = 15
        self.score = 0


