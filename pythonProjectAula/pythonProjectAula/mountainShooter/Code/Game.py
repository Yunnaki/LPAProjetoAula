#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Menu import Menu
from Code.const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()


