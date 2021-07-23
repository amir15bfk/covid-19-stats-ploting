import pygame
from pygame.transform import scale
class Plot:
    def __init__(self,x,y,data):
        self.x = x
        self.y = y
        self.set_data(data)

    def plot(self,screen):
        pygame.draw.lines(screen,(0, 0, 0), False,self.data,3)
    def process(self,inp,scale):
        out = []
        for i , j in enumerate(inp):
            out.append((self.x+i*1.8,self.y-j/scale))
        return out
    def set_data(self,data):
        max_of_data = max(data)
        scale = max_of_data / 400
        self.data = self.process(data,scale)
            