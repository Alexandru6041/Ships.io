import pygame
from ui.settings import LABELS

class Label():
    def __init__(self, surface, text, size, color):
        self.font = self.__fontsize(size)
        self.image = self.font.render(text, 1, color)
        self.surface = surface
        self.text = text
        # LABELS.append(self)
        
    def __fontsize(self, size):
        font = pygame.font.SysFont("Arial", size)
        return font
    
    def change_text(self, newtext, color="white"):
        self.image = self.font.render(newtext, 1, color)
        
    def change_font(self, font, size, color="white"):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)
    
    def draw(self, pos:tuple):
        self.surface.blit(self.image, pos)
    
    def get_size(self):
        w = self.image.get_width()
        h = self.image.get_height()
        return w, h

def show_labels():
    for label in LABELS:
        label.draw()