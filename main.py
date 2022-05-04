from ball import Ball
from bricks import Bricks
from counts import *
from my_pygame import *
from paddle import Paddle


def mainloop():
    ball = Ball((WIDTH / 2, HEIGHT / 2))
    paddle = Paddle(surface, 100, 10, WIDTH / 2, HEIGHT - 30)
    bricks = Bricks()

    while True:
        surface.fill(BLACK_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        bricks.show()
        paddle.update()
        paddle.draw()

        hit_position = ball.hit_a_brick(bricks)
        bricks.remove(hit_position)

        draw_text(surface, f"score : {bricks.score}", FONT_Microsoft_YaHei,
                  (30, HEIGHT - 30), 21, RED_COLOR)
        ball.update(paddle)
        ball.show()

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption("brick out game game")
    mainloop()
