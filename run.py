import pygame
from ui.game_manager import GameManager
from ui.screen_manager import ScreenManager
from ui.input_handler import InputHandler
from ui.screens import *
from ui.settings import *

pygame.init()
pygame.display.init()
pygame.display.set_caption(TITLE)
pygame.font.init()

window = pygame.display.set_mode((1200, 800))

input_handler = InputHandler()

screen_manager = ScreenManager()
game_manager = GameManager(input_handler, screen_manager)

screen_manager.add_screens([

])

while True:
    window.fill('white')
    screen_manager.current_screen.draw()
    pygame.display.update()