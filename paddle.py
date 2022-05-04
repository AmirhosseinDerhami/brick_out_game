import pygame

from counts import *
from my_pygame import draw_rect


class Paddle:
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h
        self.color = (0, 255, 0)
        self._rect = pygame.rect.Rect(x, y, width, height)

    def draw(self):
        draw_rect(pygame.display.get_surface(), self.color, self._rect)

    def update(self):
        # moves the obstacle by mouse
        x, y = pygame.mouse.get_pos()
        if self._rect.w / 2 <= x <= (WIDTH - self._rect.w / 2):
            self._rect.centerx = x

    def get_rect(self):
        return self._rect
