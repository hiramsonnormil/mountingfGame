import pygame as game
import pygame.mixer_music

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.menu import Menu

class Game:
    def __init__(self):
        game.init()
        self.window = game.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

if __name__ == "__main__":
    game = Game()
    game.run()
