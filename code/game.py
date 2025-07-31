import pygame as game

class Game:
    def __init__(self):
        game.init()
        self.window = game.display.set_mode((600, 480))

    def run(self):
        while True:
            menu = menu(self.window)
            menu.run()
            pass

if __name__ == "__main__":
    game = Game()
    game.run()
