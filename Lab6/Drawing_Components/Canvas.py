import matplotlib.pyplot as plt
class Canvas :
    def __init__(self):
        self.lines=[]
        
    def add_line(self,line):
        self.lines.append(line)
        
    def draw(self):
        for line in self.lines :
            x_vals = [line.start.x,line.end.x]
            y_vals = [line.start.y,line.end.x]
            plt.plot(x_vals,y_vals)
        plt.axis('equal')
        plt.show()