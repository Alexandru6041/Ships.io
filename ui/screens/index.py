from ui.game_manager import GameManager
from ui.screen import Screen


class IndexPage(Screen):
    def __init__(self, win, index:int, game_manager:GameManager):
        super(IndexPage, self).__init__(win, 'Index', index, game_manager)
    
    def draw(self):
        pass