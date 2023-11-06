import pygame

class InputHandler:
    def __init__(self, events:dict, game_manager):
        self.events = events
        self.game_manager = game_manager

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_manager.running = False
            
            elif event.type == pygame.KEYDOWN and event.key in self.events:
                self.events[event.key]()

            elif event.type == pygame.MOUSEBUTTONUP and 'mouse' in self.events:
                if event.button in self.events['mouse']:
                    self.events['mouse'][event.button](pygame.mouse.get_pos())
