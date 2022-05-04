import pygame


def rect_contain(rect_small, rect_big):
    return rect_small.top > rect_big.top and \
           rect_small.bottom < rect_big.bottom and \
           rect_small.left > rect_big.left and \
           rect_small.right < rect_big.right


def draw_text(surface, text, font_name, pos, size, color):
    font = pygame.font.SysFont(font_name, size).render(text, True, color)
    surface.blit(font, pos)


def draw_rectangle(surface, color, x, y, width, height, b_radius=5):
    return pygame.draw.rect(surface, color, pygame.Rect((x, y, width, height)), border_radius=b_radius)


def draw_rect(surface, color, rect, b_radius=5):
    return pygame.draw.rect(surface, color, rect, border_radius=b_radius)


def draw_circle(game_screen, color, pos, r, fill):
    """ if fill == 0, (default) fill the circle -
        if fill > 0, used for line thickness -
        if fill < 0, nothing will be drawn"""
    return pygame.draw.circle(game_screen, color, pos, r, fill)
