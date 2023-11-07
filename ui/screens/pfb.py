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
            }, pygame.K_SPACE: self.move_on}, game_manager)
        
        self.table = [[0 for i in range(GRID_TEMPLATE[1])] for i in range(GRID_TEMPLATE[0])]
        self.move_on_label = Label(self.win, 'You have finished your drawing! Press Space to enter the game!', 20, 'black')
        self.wall_cnt = 0
        self.treasure = None
    
    def move_on(self):
        if self.wall_cnt == 15:
            self.game_manager.start_game(self.table)
            self.game_manager.change_screen(2)

    def click_cell(self, pos:tuple[int, int]):
        if not is_in_grid(pos):
            return
        
        x0 = (WINDOW_SIZE[0] - GRID_SIZE[0]) // 2
        y0 = (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2
        grid_x = (pos[1] - y0) // CELL_SIZE[0]
        grid_y = (pos[0] - x0) // CELL_SIZE[1]
        
        if not self.table[grid_x][grid_y] and self.wall_cnt < MAX_WALL_NB:
            self.table[grid_x][grid_y] = 1
            self.wall_cnt += 1
        
        elif self.table[grid_x][grid_y]:
            self.table[grid_x][grid_y] = 100
            if self.treasure: self.table[self.treasure[0]][self.treasure[1]] = 0
            self.treasure = (grid_x, grid_y)

    
    def erase_cell(self, pos:tuple[int, int]):
        if not is_in_grid(pos):
            return
        
        x0 = (WINDOW_SIZE[0] - GRID_SIZE[0]) // 2
        y0 = (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2
        grid_x = (pos[1] - y0) // CELL_SIZE[0]
        grid_y = (pos[0] - x0) // CELL_SIZE[1]
        
        if self.table[grid_x][grid_y]:
            self.table[grid_x][grid_y] = 0
            self.wall_cnt -= 1
    
    def draw(self):
        x0 = (WINDOW_SIZE[0] - GRID_SIZE[0]) // 2
        y0 = (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2
        #Grid 
        pygame.draw.rect(self.win, 'black', ((WINDOW_SIZE[0] - GRID_SIZE[0])// 2, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2) + GRID_SIZE, 1)
        for i in range(10):
            for j in range(10):
                cell_x = x0 + j * CELL_SIZE[0]
                cell_y = y0 + i * CELL_SIZE[1]
                pygame.draw.rect(self.win, 'black', (cell_x,  cell_y) + CELL_SIZE, 1)
                if self.table[i][j]:
                    pygame.draw.rect(self.win, 'blue', (cell_x + 1, cell_y + 1, CELL_SIZE[0] - 1, CELL_SIZE[1] - 1))

                    if self.table[i][j] == 100:
                        l = Label(self.win, 'T', 18, 'yellow')
                        w, h = l.get_size()
                        l.draw((cell_x + w // 2, cell_y + h // 2))

        if self.wall_cnt == MAX_WALL_NB:
            self.move_on_label.draw((x0, y0 + GRID_SIZE[1] + 50))

        self.input_handler.handle_events()
        

def is_in_grid(pos:tuple[int, int]) -> bool:
    return (WINDOW_SIZE[0] - GRID_SIZE[0]) // 2 <= pos[0] < (WINDOW_SIZE[0] + GRID_SIZE[0]) // 2 and (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2 <= pos[1] < (WINDOW_SIZE[1] + GRID_SIZE[1]) // 2