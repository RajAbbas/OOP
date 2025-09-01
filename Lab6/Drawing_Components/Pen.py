import math
from Geometry.Line import Line
from Geometry.Point import Point
class Pen :
    def __init__(self,canvas,x=0,y=0,angle=0):
        self.canvas = canvas
        self.angle = angle
        self.x=x 
        self.y =y
    def move_forward(self,step=1):
        new_x = self.x +step * math.cos(math.radians(self.angle))
        new_y = self.y +step * math.cos(math.radians(self.angle))
        line = Line(Point(self.x,self.y),Point(new_x,new_y))
        self.canvas.add_line(line)
        self.x = new_x
        self.y = new_y
        
    def turn_left(self,angle=90):
        self.angle += angle
        
    def turn_right(self,angle=90):
        self.angle -= angle