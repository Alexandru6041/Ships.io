from .screen import Screen

class ScreenManager:
    def __init__(self):
        self.__screens = []
        self.__current_screen = 0
    
    def add_screens(self, screens:list[Screen]):
        self.__screens += screens

    def change_screen(self, screen:int):
        self.__current_screen = screen
    
    @property
    def current_screen(self) -> Screen:
        return self.__screens[self.__current_screen]