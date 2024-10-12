"""
this file is responsible for change environ statement
"""

from drones import *
import pygame as pg


class Game:
    """
    This class responsible for all events in the game
    """

    def __init__(self):
        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 60

        self.window = pg.display.set_mode((self.WIDTH, self.HIGH))
        self.clock = pg.time.Clock()

        self.master = Master()

    def draw_all(self):
        """
        drawing all objects
        """

        self.window.fill(pg.Color('black'))

        self.draw_cursor(self.window)

        # draw rectangles for test agent movement
        rect_W = 30
        rect_H = 30

        pg.draw.rect(self.window, (0, 255, 0), (100, 100, rect_W, rect_H))  # x, y, w, h
        pg.draw.rect(self.window, (0, 255, 0), (600, 600, rect_W, rect_H))
        pg.draw.rect(self.window, (0, 255, 0), (600, 100, rect_W, rect_H))
        pg.draw.rect(self.window, (0, 255, 0), (100, 600, rect_W, rect_H))
        pg.draw.rect(self.window, (0, 255, 0), (1200, 300, rect_W, rect_H))

        self.master.draw(self.window)

        pg.display.update()
        self.clock.tick(self.FPS)

    @staticmethod
    def draw_cursor(window):
        """
        draw cursor on the selected window
        :param window:
        :return: None
        """
        pg.mouse.set_visible(False)
        cursor_pos = pg.mouse.get_pos()
        pg.draw.line(window, (255, 0, 0),
                     (cursor_pos[0] + 10, cursor_pos[1] + 10),
                     (cursor_pos[0] - 10, cursor_pos[1] - 10))
        pg.draw.line(window, (255, 0, 0),
                     (cursor_pos[0] - 10, cursor_pos[1] + 10),
                     (cursor_pos[0] + 10, cursor_pos[1] - 10))

    def start_game(self):
        """
        def for start environment
        :return: None
        """

        while True:
            self.draw_all()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit


if __name__ == "__main__":
    game = Game()
    game.start_game()
