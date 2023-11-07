import time
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

    def draw(self, events=True, loser_up_to_date=False):
        left_board = Grid(self.win, (WINDOW_SIZE[0] // 2 - GRID_SIZE[0] - 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2),
                               self.game_manager.my_board, {1:'blue', -1:'gray', 100:'yellow'})
        
        right_board = Grid(self.win, (WINDOW_SIZE[0] // 2 + 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2),
                               self.game_manager.other_board, {-1:'gray', 1:'blue', 100:'yellow'})
        left_board.draw()
        right_board.draw()
        
        if self.game_manager.has_won:
            pygame.draw.polygon(self.win, 'yellow', ((WINDOW_SIZE[0] // 2 + 8, WINDOW_SIZE[1] // 2), (WINDOW_SIZE[0] // 2 - 8, WINDOW_SIZE[1] // 2 - 10), (WINDOW_SIZE[0] // 2 - 8, WINDOW_SIZE[1] // 2 + 10)))
            self.input_handler.events['mouse'] = {1: self.handle_click}
            
        else: 
            pygame.draw.polygon(self.win, 'red', ((WINDOW_SIZE[0] // 2 - 8, WINDOW_SIZE[1] // 2), (WINDOW_SIZE[0] // 2 + 8, WINDOW_SIZE[1] // 2 - 10), (WINDOW_SIZE[0] // 2 + 8, WINDOW_SIZE[1] // 2 + 10)))
            self.input_handler.events = {} 
            pygame.display.update()
            if not loser_up_to_date:
                changes = self.game_manager.client.update_board()
                for i in range(10):
                    for j in range(10):
                        if changes[i][j] == 100:
                            l = Label(self.win, 'YOU LOST!', 50, 'red')
                            w, h = l.get_size()
                            l.draw(((WINDOW_SIZE[0] -  w)// 2, (WINDOW_SIZE[1] - h) // 2))
                            pygame.display.update()
                            time.sleep(10)
                            self.game_manager.client.close()
                            self.game_manager.running = False
                            return
                        
                        if not self.game_manager.my_board[i][j] and changes[i][j]:
                            self.game_manager.my_board[i][j] = changes[i][j]
                
                
                self.draw(loser_up_to_date=True)
                pygame.display.update()
                time.sleep(5)
                self.game_manager.change_screen(2)
        
        if events: 
            self.input_handler.handle_events()
        
    def handle_click(self, pos:tuple[int, int]): # ATAC
        if not is_in_grid(pos):
            return
        x, y = (WINDOW_SIZE[0] // 2 + 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2)
        grid_x = (pos[1] - y) // CELL_SIZE[0]
        grid_y = (pos[0] - x) // CELL_SIZE[1]
        
        if not self.game_manager.other_board[grid_x][grid_y]:
            self.game_manager.client.attack((grid_x, grid_y))
            changes = self.game_manager.client.update_board()
            for i in range(10):
                for j in range(10):
                    if changes[i][j] == 100:
                        l = Label(self.win, 'YOU WON!', 50, 'green')
                        w, h = l.get_size()
                        l.draw(((WINDOW_SIZE[0] -  w)// 2, (WINDOW_SIZE[1] - h) // 2))
                        pygame.display.update()
                        time.sleep(10)
                        self.game_manager.client.close()
                        self.game_manager.running = False
                        return
                    
                    if not self.game_manager.other_board[i][j] and changes[i][j]:
                        self.game_manager.other_board[i][j] = changes[i][j]
            
            self.draw(events=False)
            pygame.display.update()
            time.sleep(5)
            self.game_manager.change_screen(2)
        
    
def is_in_grid(pos:tuple[int, int]) -> bool:
    x, y = (WINDOW_SIZE[0] // 2 + 60, (WINDOW_SIZE[1] - GRID_SIZE[1]) // 2)
    
    return x <= pos[0] < x + GRID_SIZE[0] and y <= pos[1] < y + GRID_SIZE[1]