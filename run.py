import pygame
from ui.game_manager import GameManager
from ui.screen_manager import ScreenManager
from ui.screens.game_area import GameArea
from ui.screens.index import IndexPage
from ui.screens.pfb import Pfb
from ui.screens.question import QuestionScreen
from ui.settings import *

pygame.init()
pygame.display.init()
pygame.display.set_caption(TITLE)
pygame.font.init()

window = pygame.display.set_mode(WINDOW_SIZE)

screen_manager = ScreenManager()
game_manager = GameManager(screen_manager)

screen_manager.add_screens([
    Pfb(window, 0, game_manager),
    GameArea(window, 1, game_manager),
    QuestionScreen(window, 2, game_manager),
    IndexPage(window, 3, game_manager),
])

game_manager.change_screen(3)

while game_manager.running:
    window.fill('white')
    screen_manager.current_screen.draw()
    pygame.display.update()