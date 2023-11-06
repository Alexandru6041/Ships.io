from ui.game_manager import GameManager
from ui.input_handler import InputHandler
from ui.screen import Screen
from ui.elements.label import Label
from ui.elements.button import Button
import pygame
from ui.settings import *

class Pfb(Screen):
    def __init__(self, win, index:int, game_manager:GameManager):
        super(Pfb, self).__init__(win, 'Index', index, game_manager)
        self.input_handler = InputHandler({'mouse':{
            1: self.click_cell,
            3: self.erase_cell
            }}, game_manager)
        
        self.table = [[0 for i in range(GRID_TEMPLATE[1])] for i in range(GRID_TEMPLATE[0])]
    
    def click_cell(self, pos:tuple[int, int]):
        x0 = (WINDOW_SIZE[0] - GRID_SIZE[0]) // 2
        y0 = (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2
        grid_x = (pos[1] - y0) // CELL_SIZE[0]
        grid_y = (pos[0] - x0) // CELL_SIZE[1]
        
        self.table[grid_x][grid_y] = 1
    
    def erase_cell(self, pos:tuple[int, int]):
        x0 = (WINDOW_SIZE[0] - GRID_SIZE[0]) // 2
        y0 = (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2
        grid_x = (pos[1] - y0) // CELL_SIZE[0]
        grid_y = (pos[0] - x0) // CELL_SIZE[1]
        
        self.table[grid_x][grid_y] = 0
    
    def draw(self):
        #Grid
        pygame.draw.rect(self.win, 'black', (400, 200, 400, 400), 1)
        for i in range(10):
            for j in range(10):
                pygame.draw.rect(self.win, 'black', (400 + i * 40, 200 + j * 40, 40, 40), 1)
                if self.table[i][j]:
                    pygame.draw.rect(self.win, 'blue', (400 + j * 40 + 1, 200 + i * 40 + 1, 39, 39))
                
        self.input_handler.handle_events()
        
        