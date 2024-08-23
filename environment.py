# this file is responsible for change environ statement

import pygame as pg
from drones import *


class Game:
    """
    This class responsible for all events in the game
    """

    def __init__(self):
        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 60

    def draw_all(self):
        """
        drawing all objects
        """
        window = pg.display.set_mode((self.WIDTH, self.HIGH))
        clock = pg.time.Clock()

        window.fill(pg.Color('black'))

        self.draw_cursor(window)

        pg.display.update()
        clock.tick(self.FPS)

    @staticmethod
    def draw_cursor(window):
        pg.mouse.set_visible(False)
        cursor_pos = pg.mouse.get_pos()
        pg.draw.line(window, (255, 0, 0),
                     (cursor_pos[0] + 10, cursor_pos[1] + 10),
                     (cursor_pos[0] - 10, cursor_pos[1] - 10))
        pg.draw.line(window, (255, 0, 0),
                     (cursor_pos[0] - 10, cursor_pos[1] + 10),
                     (cursor_pos[0] + 10, cursor_pos[1] - 10))

    def start_game(self):

        while True:
            self.draw_all()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit


if __name__ == "__main__":
    game = Game()
    game.start_game()
