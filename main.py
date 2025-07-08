import pygame as game

game.init()
print("Game init")
window = game.display.set_mode(size=(600, 480))
print("Game End")

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            quit()