import pygame
from ui.elements.label import Label
from ui.input_handler import InputHandler
from ui.screen import Screen
from ui.settings import *

class Grid:
    def __init__(self, win, pos:tuple[int, int], m:list[list[int]], color_map:dict[int, str]):
        self.win = win
        self.m = m
        self.color_map = color_map
        self.pos = pos
    
    def draw(self):
        x0, y0 = self.pos
        #Grid 
        pygame.draw.rect(self.win, 'black', self.pos + GRID_SIZE, 1)

        for i in range(10):
            for j in range(10):
                cell_x = x0 + j * CELL_SIZE[0]
                cell_y = y0 + i * CELL_SIZE[1]
                pygame.draw.rect(self.win, 'black', (cell_x,  cell_y) + CELL_SIZE, 1)
                if self.m[i][j]:
                    pygame.draw.rect(self.win, self.color_map[self.m[i][j]], (cell_x + 1, cell_y + 1, CELL_SIZE[0] - 1, CELL_SIZE[1] - 1))

                    if self.m[i][j] == 100:
                        l = Label(self.win, 'T', 18, 'yellow')
                        w, h = l.get_size()
                        l.draw((cell_x + w // 2, cell_y + h // 2))

class GameArea(Screen):
    def __init__(self, win, index:int, game_manager):
        super(GameArea, self).__init__(win, 'GameArea', index, game_manager)
        self.input_handler = InputHandler({}, game_manager)

    def draw(self):
        left_board = Grid(self.win, (WINDOW_SIZE[0] // 2 - GRID_SIZE[0] - 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2),
                               self.game_manager.my_board, {1:'blue', 2:'red'})
        
        right_board = Grid(self.win, (WINDOW_SIZE[0] // 2 + 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2),
                               self.game_manager.other_board, {2:'blue'})
        left_board.draw()
        right_board.draw()
        self.input_handler.handle_events()