from ui.screen_manager import ScreenManager

class GameManager:
    def __init__(self, screen_manager:ScreenManager):
        self.running = True
        self.screen_manager = screen_manager
        self.my_table = [[0 for i in range(10)] for i in range(7)] + [[1 for i in range(10)] for i in range(3)]
        self.other_table = [[0 for i in range(10)] for i in range(10)]
        self.other_table[4][3] = self.other_table[4][5] = self.other_table[3][4] = self.other_table[2][0] = 2
    
    def change_screen(self, index:int):
        self.screen_manager.change_screen(index)