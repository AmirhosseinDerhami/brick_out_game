import pygame.display

from counts import *
from my_pygame import draw_circle


class Ball:
    def __init__(self, pos):
        self.live = True
        radius = 5
        self._vel_x = 2
        self._vel_y = 2.9
        self.ball = draw_circle(pygame.display.get_surface(), WHITE_COLOR, pos, radius, 0)

    def show(self):
        draw_circle(pygame.display.get_surface(), WHITE_COLOR, self.ball.center, self.ball.w / 2, 0)

    def _move(self):
        if self.live:
            self.ball.centerx += self._vel_x
            self.ball.centery += self._vel_y

    def _bouncing(self, side):
        if side == "vertical":  # right screen wall bounce
            self._vel_x *= -1

        if side == "horizontal":  # top or bottom wall bounce
            self._vel_y *= -1

    def update(self, paddle):
        self.update_hit_insides()
        self.update_hit_outsides(paddle.get_rect())
        self._move()

    def hit_a_brick(self, bricks):
        for row in range(ROWS):
            for col in range(COLS):
                brick = bricks.get((row, col))
                if brick is not None:
                    if not brick.hit:
                        if self.update_hit_outsides(brick.get_rect()):
                            return row, col

        return None

    def update_hit_insides(self):
        ball = self.ball
        if ball.left < 0 or ball.right > WIDTH:  # right screen wall bounce
            self._bouncing("vertical")
            return True
        if ball.top < 0:  # top  wall bounce
            self._bouncing("horizontal")
            return True
        if ball.bottom > HEIGHT:  # top or bottom wall bounce
            self.live = False
            return True

        return False

    def update_hit_outsides(self, obstacle):
        ball = self.ball
        collision_tolerance = 5

        if ball.colliderect(obstacle):
            if abs(ball.top - obstacle.bottom) < collision_tolerance and self._vel_y < 0:
                self._bouncing("horizontal")
            if abs(ball.bottom - obstacle.top) < collision_tolerance and self._vel_y > 0:
                self._bouncing("horizontal")
            if abs(ball.right - obstacle.left) < collision_tolerance and self._vel_x > 0:
                self._bouncing("vertical")
            if abs(ball.left - obstacle.right) < collision_tolerance and self._vel_x < 0:
                self._bouncing("vertical")
            return True

        return False
