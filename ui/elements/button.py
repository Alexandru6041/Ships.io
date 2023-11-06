import pygame
from ui.input_handler import InputHandler
from .label import Label

class Button:
    def __init__(self, surface, pos:tuple, size:tuple, font_size:int, label:str, color:str, on_press):
        self.surface = surface
        self.pos = pos
        self.size = size
        self.color = color
        self.label = Label(surface, label, font_size, 'white')
        self.__on_press = on_press

    def draw(self):
        w, h = self.label.get_size()
        pygame.draw.rect(self.surface, self.color, self.pos + self.size)
        self.label.draw((self.pos[0] + (self.size[0] - w) / 2,
                         self.pos[1] + (self.size[1] - h) / 2))

    def press(self):
        self.__on_press()