import datetime
from ui.elements.button import Button
from ui.elements.label import Label
from ui.input_handler import InputHandler
from ui.game_manager import GameManager
from ui.screen import Screen
from ui.settings import *
import time

class QuestionScreen(Screen):
    def __init__(self, win, index:int, game_manager):
        super(QuestionScreen, self).__init__(win, 'QuestionScreen', index, game_manager)
        self.input_handler = InputHandler({'mouse': {1: self.handle_clicks}}, game_manager)
    
    def draw(self):
        self.q = self.game_manager.question

        statement = Label(self.win, self.q.statement, 30, 'black')
        w = statement.get_size()[0]
        statement.draw(((WINDOW_SIZE[0] - w) // 2, 30))

        self.buttons = []
        w = WINDOW_SIZE[0] // 3
        h = 100

        y = 70

        for choice in self.q.choices:
            b = Button(self.win, ((WINDOW_SIZE[0] - w) // 2, y), (w, h), 20, choice, '#C7C7FF', None)
            b.draw()
            self.buttons.append(b)
            y += 115
    
        self.input_handler.handle_events()
        
    def handle_clicks(self, pos):
        print(2)
        for x, button in enumerate(self.buttons):
            if (button.pos[0] <= pos[0] <= button.pos[0] + button.size[0] and
                button.pos[1] <= pos[1] <= button.pos[1] + button.size[1]):
                r = self.game_manager.client.send_a(x, (self.game_manager.time_start - datetime.datetime.now()).total_seconds())
                if(r == "rerun"):
                    Label(self.win, "Intrebarea se va repeta", 25, "black").draw((WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]- CELL_SIZE[1]))
                    time.sleep(1.5)
                    GameManager.change_screen(2)
                elif(r == "true"):
                    Label(self.win, "Raspuns gresit", 25, "black").draw((WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]- CELL_SIZE[1]))
                    time.sleep(1.5)
                    GameManager.change_screen(1)
                elif(r == "false"):
                    Label(self.win, "Raspuns corect", 25, 'black').draw((WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]- CELL_SIZE[1]))
                    time.sleep(1.5)
                    GameManager.change_screen(1)