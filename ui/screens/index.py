# from ui.game_manager import GameManager
from ui.input_handler import InputHandler
from ui.screen import Screen
from ui.elements.label import Label
from ui.elements.button import Button



class IndexPage(Screen):
    def __init__(self, win, index:int, game_manager):
        super(IndexPage, self).__init__(win, 'Index', index, game_manager)
        self.play_button = Button(self.win, (100, 100), (200, 100), 20, 'PLAY', 'blue', lambda:print(1))
        self.input_handler = InputHandler({'mouse':{1:self.handle_clicks}}, game_manager)

    def draw(self):
        self.play_button.draw()
        self.input_handler.handle_events()
    
    def handle_clicks(self, pos:tuple):
        if (self.play_button.pos[0] <= pos[0] <= self.play_button.pos[0] + self.play_button.size[0] and
            self.play_button.pos[1] <= pos[1] <= self.play_button.pos[1] + self.play_button.size[1]):
            self.play_button.press()