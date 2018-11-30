import numpy as np

from environment import a_star


class Agent:
    direction = None
    shortest_path = None
    next_position = 1

    def __init__(self, start, end, environment):
        self.start = start
        self.end = end
        self.environment = environment

    def get_direction(self):
        x = self.end(0) - self.start(0)
        y = self.start(0) - self.start(1)
        return np.arctan2(y, x) * 180 / np.pi

    def set_shortest_path(self):
        self.shortest_path = a_star.astar(self.environment, self.start, self.end)

    def move(self):
        self.start = self.shortest_path[self.next_position]
        self.next_position += 1

    def check_if_finish(self):
        if self.end == self.start:
            return True
        else:
            return False




    # def get_next_position(self):
    #     direction = self.get_direction()
    #     if -22.5 < direction <= 22.5:
    #         print('x')
    #         self.x += 1
    #     elif 22.5 < direction <= 67.5:
    #         print("x,y")
    #         self.x += 1
    #         self.y += 1
    #     elif 67.5 < direction <= 112.5:
    #         print('y')
    #         self.y += 1
    #     elif 112.5 < direction <= 157.5:
    #         print("-x,y")
    #         self.x -= 1
    #         self.y += 1
    #     elif 157.5 < direction <= 180 or -180 <= direction <= -157.5:
    #         print("-x")
    #         self.x -= 1
    #     elif -157.5 < direction <= -112.5:
    #         print("-x,-y")
    #         self.x -= 1
    #         self.y -= 1
    #     elif -112.5 < direction <= -67.5:
    #         print("-y")
    #         self.y -= 1
    #     elif -67.5 < direction <= 22.5:
    #         print("x,-y")
    #         self.x += 1
    #         self.y -= 1

    def check_if_done(self):
        pass


def bobo():
    pass


