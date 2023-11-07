class Screen:
    def __init__(self, win, name:str, index:int, game_manager):
        self.win = win
        self.name = name
        self.index = index
        self.game_manager = game_manager

    def draw(self):
        pass