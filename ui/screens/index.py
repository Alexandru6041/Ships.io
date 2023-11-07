from ui.input_handler import InputHandler
from ui.screen import Screen
from ui.elements.label import Label
from ui.elements.button import Button
from ui.settings import *



class IndexPage(Screen):
    def __init__(self, win, index:int, game_manager):
        super(IndexPage, self).__init__(win, 'Index', index, game_manager)
        self.input_handler = InputHandler({'mouse':{1:self.handle_clicks}}, game_manager)

    def draw(self):
        title = Label(self.win, TITLE, 50, 'blue')
        w = title.get_size()[0]
        title.draw(((WINDOW_SIZE[0] - w) // 2, WINDOW_SIZE[1] // 2 - 300))
        
        subtitle = Label(self.win, 'by RebootX', 30, 'black')
        w = subtitle.get_size()[0]
        subtitle.draw(((WINDOW_SIZE[0] - w) // 2, WINDOW_SIZE[1] // 2 - 200))
        
        self.play_button = Button(self.win, (WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 2 + 50), (200, 100), 20, 'PLAY', 'blue', lambda:self.game_manager.change_screen(0))
        self.play_button.draw()
        self.input_handler.handle_events()
    
    def handle_clicks(self, pos:tuple):
        if (self.play_button.pos[0] <= pos[0] <= self.play_button.pos[0] + self.play_button.size[0] and
            self.play_button.pos[1] <= pos[1] <= self.play_button.pos[1] + self.play_button.size[1]):
            self.play_button.press()