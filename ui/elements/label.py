import pygame
from ui.settings import LABELS

class Label():
    def __init__(self, screen, text, x, y, size, color):
        self.font = self.__fontsize(size)
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text
        LABELS.append(self)
        
    def __fontsize(self, size):
        font = pygame.font.SysFont("Arial", size)
        return font
    
    def change_text(self, newtext, color="white"):
        self.image = self.font.render(newtext, 1, color)
        
    def change_font(self, font, size, color="white"):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)
    
    def draw(self):
        self.screen.blit(self.image, (self.rect))

# if __name__ == "__main__":
#     win = pygame.display.set_mode((600, 600))
    
#     Label = (win, "hello world", 100, 100, 36)
#     first = Label(win, "Ships.io", 100, 200, 24, color = "blue")
#     first.change_font("Arial", 40, "blue")
#     ok = 1
#     while ok:
#         win.fill(0)
#         Label.show_labels()
#         pygame.display.quit()