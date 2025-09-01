from Drawing_Components.Canvas import Canvas
from Drawing_Components.Pen import Pen

class Turtle:
    def __init__(self):
        self.canvas = Canvas()
        self.pen = Pen(self.canvas)
        
    def run(self,commands):
        for cmd in commands:
            cmd.execute(self.pen)
        self.canvas.draw()