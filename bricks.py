import numpy as np
import pygame

from counts import *
from my_pygame import draw_rect


class Brick:
    def __init__(self, x, y, w, h):
        self._rect = pygame.rect.Rect(x, y, w, h)
        self.hit = False

    def get_rect(self):
        return self._rect


class Bricks:
    def __init__(self):
        self.bricks = np.empty((ROWS, COLS), dtype=Brick)
        self.color = PURPLE_COLOR
        self.score = 0
        for row in range(ROWS):
            for col in range(COLS):
                brick = Brick(col * WIDTH_SQUARE + (col + 1) * LEN_BETWEEN_SQUARES,
                              row * HEIGHT_SQUARE + (row + 1) * LEN_BETWEEN_SQUARES,
                              WIDTH_SQUARE, HEIGHT_SQUARE)
                self.bricks[row, col] = brick

    def remove(self, hit_position):
        if hit_position is not None:
            self.bricks[hit_position].hit = True

    def show(self):
        self.score = 0
        for row in self.bricks:
            for brick in row:
                if brick is not None:
                    if not brick.hit:
                        draw_rect(pygame.display.get_surface(), self.color, brick.get_rect(), 2)
                    else:
                        self.score += 10

    def set(self, value, pos):
        self.bricks[pos] = value

    def get(self, pos):
        return self.bricks[pos]

    def num_score(self):
        return self.score
