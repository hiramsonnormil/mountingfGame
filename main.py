import time

import pygame as game

game.init()
print("Game init")
window = game.display.set_mode(size=(600, 480))

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            print("espera .....")
            print("jogo fechado")
            time.sleep(2)
            quit()