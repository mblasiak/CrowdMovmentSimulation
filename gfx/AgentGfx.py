from OpenGL.GL import *
from math import *
from model.agent.Agent import Agent

class AgentGfx:
    def __init__(self, position: [float, float], map_position: [int, int], angle: float, color: [float, float, float],
                 direction, maze, direct):
        self.map_position = map_position
        self.position = position
        self.angle = radians(angle)
        self.color = color
        exits=list( zip(range(40,60),[98]*20))
        self.agent = Agent((map_position[0], map_position[1]),exits ,3 , 2, 1, direct, maze)
        self.fx_pos=(0, 0)

    def move(self):
        result = self.agent.move()
        return result

    def draw(self, radius):
        direction = [cos(self.angle) + self.position[0], sin(self.angle) + self.position[1]]

        glColor3f(self.color[0], self.color[1], self.color[2])

        # draw circle

        posx, posy = self.fx_pos
        sides = 64

        # draw circle filling
        glBegin(GL_POLYGON)
        for vertex in range(sides):
            angle = float(vertex) * 2.0 * pi / sides
            glVertex2f(cos(angle) * radius + posx, sin(angle) * radius + posy)
        glEnd()

        # draw circle outline
        glLineWidth(0.1)
        glColor3f(1.0, 1.0, 1.0)

        glBegin(GL_LINE_LOOP)
        for vertex in range(sides):
            angle = float(vertex) * 2.0 * pi / sides
            glVertex2f(cos(angle) * radius + posx, sin(angle) * radius + posy)
        glEnd()

        # draw line
        vec = [(direction[0] - self.position[0]), (direction[1] - self.position[1])]

        vec_len = sqrt(pow(vec[0], 2) + pow(vec[1], 2))
        vec[0] = vec[0] / vec_len * radius
        vec[1] = vec[1] / vec_len * radius

        glLineWidth(0.1)
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + vec[0], self.position[1] + vec[1])
        glEnd()

