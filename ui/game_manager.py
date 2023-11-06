from .input_handler import InputHandler
from .screen_manager import ScreenManager


class GameManager:
    def __init__(self, input_handler:InputHandler, screen_manager:ScreenManager):
        self.input_handler = input_handler
        self.screen_manager = screen_manager