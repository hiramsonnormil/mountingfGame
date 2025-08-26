import pygame as game
import pygame.mixer_music

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.level import Level
from code.menu import Menu
from code.Const import MENU_OPTION
class Game:
    def __init__(self):
        game.init()
        self.window = game.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return =  menu.run()
            
            if menu_return in [MENU_OPTION[0],[ MENU_OPTION[1]],[MENU_OPTION[2]]]:
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
        
