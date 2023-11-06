import pygame
from ui.game_manager import GameManager
from ui.screen_manager import ScreenManager
from ui.screens.index import IndexPage
from ui.screens.pfb import Pfb
from ui.settings import *

pygame.init()
pygame.display.init()
pygame.display.set_caption(TITLE)
pygame.font.init()

window = pygame.display.set_mode((1200, 800))

screen_manager = ScreenManager()
game_manager = GameManager()

screen_manager.add_screens([
    # IndexPage(window, 0, game_manager),
    Pfb(window, 0, game_manager)
])

while game_manager.running:
    window.fill('white')
    screen_manager.current_screen.draw()
    pygame.display.update()