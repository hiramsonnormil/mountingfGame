#!/usr/bin/python
# -*- coding: utf-8 -*-4
import pygame
from pygame import Surface, Rect, font
import pygame.image

from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('../asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load('../asset/ai-meu-cuzin.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "Mounting", (255, 128, 0), (WIN_WIDTH / 2, 70))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: font.Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
