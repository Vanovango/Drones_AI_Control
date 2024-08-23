import pygame as pg
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_window import Ui_MainWindow


class Master:
    """
    This class responsible for all actions and settings of drone-master
    """

    def __init__(self):
        self.ui = Ui_MainWindow()

        self.icon = pg.image.load('./img/MASTER_drone.png')
        # self.SPEED = eval(f"{self.ui.lineEdit_speed.text()} // 5")

        self.SPEED = 100 // 5

        self.n_master = 0
        self.coordinates = []

    def set_n_master(self, n_salve):
        """
        set needed number of master drones
        """
        self.n_master = n_salve
        self.coordinates = [[300 * (i + 1), 300 * (i + 1)] for i in range(self.n_master)]

    def draw_master(self, window):
        for i in range(self.n_master):
            window.blit(self.icon, self.coordinates[i])
            circle_center = (self.coordinates[i][0] + 20, self.coordinates[i][1] + 20)
            pg.draw.circle(surface=window, color=(0, 0, 255), radius=3000 // 20, center=circle_center, width=1)

    def move(self, event):
        """
        This method is responsible for moving masters
        """
        if event.key == pg.K_UP:
            self.coordinates[0][1] -= self.SPEED
        elif event.key == pg.K_DOWN:
            self.coordinates[0][1] += self.SPEED
        elif event.key == pg.K_RIGHT:
            self.coordinates[0][0] += self.SPEED
        elif event.key == pg.K_LEFT:
            self.coordinates[0][0] -= self.SPEED


class Slave:
    """
    This class responsible for all actions and settings of slave drone
    """

    def __init__(self):
        self.icon = pg.image.load('./img/SLAVE_drone.png')
        self.SPEED = 10

        self.n_slave = 0
        self.coordinates = []

    def set_n_salve(self, n_salve):
        """
        set needed number of slave drones
        """
        self.n_slave = n_salve
        self.coordinates = [[50 * (i + 1), 50 * (i + 1)] for i in range(self.n_slave)]

    def move(self, event):
        """
        This method is responsible for moving slaves
        """
        if event.key == pg.K_w:
            self.coordinates[0][1] -= self.SPEED
        elif event.key == pg.K_s:
            self.coordinates[0][1] += self.SPEED
        elif event.key == pg.K_d:
            self.coordinates[0][0] += self.SPEED
        elif event.key == pg.K_a:
            self.coordinates[0][0] -= self.SPEED


class Game:
    """
    This class responsible for all events in the game
    """

    def __init__(self):
        self.WIDTH = 1280
        self.HIGH = 720
        self.FPS = 120

        self.slave = Slave()
        self.slave.set_n_salve(3)

        self.master = Master()
        self.master.set_n_master(1)

    def draw_all(self):
        """
        drawing all objects
        """
        window = pg.display.set_mode((self.WIDTH, self.HIGH))
        clock = pg.time.Clock()

        window.fill(pg.Color('black'))

        self.slave.draw_slave(window)
        self.master.draw_master(window)

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
                elif event.type == pg.KEYDOWN:
                    self.slave.move(event)
                    self.master.move(event)
                # self.master.move()

# if __name__ == '__main__':
#     game = Game()
#     game.start_game()
