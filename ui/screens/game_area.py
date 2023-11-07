import pygame
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
                if self.m[i][j]:
                    pygame.draw.rect(self.win, self.color_map[self.m[i][j]], (x0 + j * CELL_SIZE[0] + 1, y0 + i * CELL_SIZE[1] + 1, CELL_SIZE[0] - 1, CELL_SIZE[1] - 1))
                
                pygame.draw.rect(self.win, 'black', (x0 + j * CELL_SIZE[0],  y0 + i * CELL_SIZE[1]) + CELL_SIZE, 1)

class GameArea(Screen):
    def __init__(self, win, index:int, game_manager):
        super(GameArea, self).__init__(win, 'GameArea', index, game_manager)
        self.input_handler = InputHandler({}, game_manager)

        self.left_board = Grid(self.win, (WINDOW_SIZE[0] // 2 - GRID_SIZE[0] - 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2),
                               self.game_manager.my_board, {1:'blue', 2:'red'})
        
        self.right_board = Grid(self.win, (WINDOW_SIZE[0] // 2 + 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2),
                               self.game_manager.other_board, {2:'blue'})

    def draw(self):
        self.left_board.draw()
        self.right_board.draw()
        self.input_handler.handle_events()