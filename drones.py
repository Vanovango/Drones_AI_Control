"""
this file is responsible for the movement of drones depending on the selected action
"""

import pygame as pg


class Drone:
    """
    main class for 2 types of drones
    """

    def __init__(self):
        """
        initialize main characteristics
        """
        self.retransmission_radius = 200
        self.speed = 20

        # global DRONE, DRONES_RECT
        self.DRONES = {'master': {}, 'slave': {}}
        self.DRONES_RECT = {'master': {}, 'slave': {}}
        self.last_master_id = 1
        self.last_slave_id = 1

    def move(self, action, object_rect):
        """
        move drone by given action
        :param action: chose movement direction
        :param object_rect: rect of drone witch must move
        :return: just move drone by given action
        """
        # dict of possible actions for drone movement
        actions = {
            'up': object_rect.move_ip(0, -self.speed),
            'down': object_rect.move_ip(0, +self.speed),
            'left': object_rect.move_ip(-self.speed, 0),
            'right': object_rect.move_ip(+self.speed, 0),
            'stay': object_rect.move_ip(0, 0)
        }
        return actions[action]

    def draw(self, window):
        """
        draw drones on selected area
        :param window: window there drone will be drawn
        :return: new frame on drawing window
        """
        window.blit(self.DRONES['master'][1], self.DRONES_RECT['master'][1])  # draw DRONES
        pg.draw.circle(window, pg.Color('blue'),
                       self.DRONES_RECT['master'][1].center, self.retransmission_radius, 2)  # draw circle around DRONES


class Master(Drone):
    """
    This class responsible for all actions and settings of drone-master
    """

    def __init__(self):
        super().__init__()
        self.icon = pg.image.load('./images/MASTER_drone.png')
        # generate master position on center of game window

        self.DRONES['master'] = {
            self.last_master_id: self.icon
        }

        # TODO add settings to generate drones positions
        self.DRONES_RECT['master'] = {
            self.last_master_id: self.DRONES['master'][1].get_rect(centerx=640, centery=360)
        }

        self.last_master_id += 1


class Slave(Drone):
    """
    This class responsible for all actions and settings of slave drone
    """

    def __init__(self):
        super().__init__()
        self.icon = pg.image.load('./img/SLAVE_drone.png')
        self.number_of_slave_drones = 0
        self.slave_drones = {}

    def set_number_of_slave_drones(self, number):
        """
        set number of slave drones and fill slave_drones dictionary
        :param number: number of slave drones
        :param number:
        :return:
        """
        for i in range(1, number + 1):
            # generate slaves positions on main diagonal
            self.slave_drones[i] = self.icon.get_rect(centralx=75 * i, centraly=50 * i)
