import datetime
from server.client import Client
from ui.screen_manager import ScreenManager
from ui.settings import *

class GameManager:
    def __init__(self, screen_manager:ScreenManager):
        self.running = True
        self.screen_manager = screen_manager
        self.my_table = [[0 for i in range(10)] for i in range(7)] + [[1 for i in range(10)] for i in range(3)]
        self.time_start = datetime.datetime.now()
    
    def change_screen(self, index:int):
        if index == 2:
            self.question = self.client.recv_q()
            
        self.screen_manager.change_screen(index)
        self.time_start = datetime.datetime.now()
    
    def start_game(self, board:list[list[int]]):
        self.my_board = board
        self.other_board = [[0 for i in range(10)] for i in range(10)]
        
        self.client = Client(HOST_IP, HOST_PORT)
        self.client.send_board(board)