from math import *
import glfw
from OpenGL.GL import *
import os
import random
import re

from src.agent.Agent import Agent
from src.direction_map.DirectionMap import DirectionMap
from src.environment.environment_enum import Env
from src.environment.line import Point


def get_current_working_dir():
    print(os.path.dirname(os.path.realpath(__file__)))


def load_map_from_file(map_filename: str):
    with open(map_filename) as text_file:
        return [[int(x) for x in line.split()] for line in text_file]


def load_direction_from_file(directions_filename: str):
    with open(directions_filename) as text_file:
        content = text_file.readlines()
    direction = []
    for line in content:
        splitted = re.split("\) \(|\) |\(| |, |\n", line)
        splitted = splitted[1::]
        splitted = splitted[:-2 or None]
        points = []
        pos_x = -1
        candidate = False
        for x in splitted:
            if candidate:
                candidate = False
                points.append((pos_x, int(x)))
            elif x == '':
                continue
            elif x == 'obstacle':
                points.append(Env.OBSTACLE)
            elif x == 'exit':
                points.append(Env.EXIT)
            else:  # x is a number
                candidate = True
                pos_x = int(x)
        direction.append(points)
    return direction


class AgentGfx:
    def __init__(self, position: [float, float], map_position: [int, int], angle: float, color: [float, float, float],
                 direction, maze, direct):
        self.map_position = map_position
        self.position = position
        self.angle = radians(angle)
        self.color = color
        exits=list( zip(range(40,60),[98]*20))
        self.agent = Agent((map_position[0], map_position[1]),exits , 3, 3, 2, direct, maze)
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


class AgentManager:
    def __init__(self, initial_tile_size: [float, float], client_width: int, client_height: int, map_offset: int,
                 direction_map, exit, maze, direct):
        self.agent_list = list()
        self.tile_size = initial_tile_size
        self.agent_radius = (initial_tile_size[1] - initial_tile_size[1] / 5) / 2
        self.width = client_width
        self.height = client_height
        self.offset = map_offset
        self.direction_map = direction_map
        self.exit_points = exit
        self.maze = maze
        self.direct = direct

    def set_client_tile_size(self, client_width: int, client_height: int, tile_size: [float, float]):
        self.width = client_width
        self.height = client_height
        self.tile_size = tile_size
        self.agent_radius = (tile_size[1] - tile_size[1] / 5) / 2

        for agent in self.agent_list:
            correct_pos = [
                0 + self.offset + 1 + (agent.map_position[1] * self.tile_size[0]) + (self.tile_size[0] / 2),
                self.height - self.offset - 1 - (agent.map_position[0] * self.tile_size[1]) - (self.tile_size[1] / 2)
            ]
            agent.position = correct_pos

    def draw_all(self):
        for agent in self.agent_list:
            agent.draw(self.agent_radius)

    def add_new(self, position: [int, int], angle: float, color: [float, float, float]):
        for agent in self.agent_list:
            if agent.map_position == position:
                print("Nie mozna dodac agenta na tej pozycji!")
                return

        correct_pos = [
            0 + self.offset + 1 + (position[1] * self.tile_size[0]) + (self.tile_size[0] / 2),
            self.height - self.offset - 1 - (position[0] * self.tile_size[1]) - (self.tile_size[1] / 2)
        ]

        dir_x, dir_y = self.direction_map[position[0]][position[1]]

        self.agent_list.append(AgentGfx(correct_pos, position, angle, color, [dir_x, dir_y], maze, direct))

    def step(self):
        for agent in self.agent_list:
            if agent.move():
                self.agent_list.remove(agent)

            agent.map_position = agent.agent.current_pos
            agent.fx_pos = [
                0 + self.offset + 1 + (agent.map_position[1] * self.tile_size[0]) + (self.tile_size[0] / 2),
                self.height - self.offset - 1 - (agent.map_position[0] * self.tile_size[1]) - (
                            self.tile_size[1] / 2)
            ]

            agent.position = agent.fx_pos


if not glfw.init():
    exit(1)

window = glfw.create_window(1280, 720, "Modelowanie i Symulacja Systemów - Symulacja (0 FPS)", None, None)
glfw.make_context_current(window)

if not window:
    glfw.terminate()
    exit(1)

camera_position = [0.5, 0.5, 0]

maze = load_map_from_file("resources/dobry_maze100na100.txt")

exit_points = []
for i in range(40, 60):
    exit_points.append(Point(99, i))

# directions = direction_map(maze, exit_points, 1)
directions = load_direction_from_file("resources/direction_map100na100.txt")
direct = DirectionMap(directions)

free_color = [25, 25, 25]
collision_color = [128, 0, 0]

w_prev = 1280
h_prev = 720

offset = 20

# tile size
t_s = [(w_prev - 2 * (offset + 1)) / len(maze[0]), (h_prev - 2 * (offset + 1)) / len(maze)]

agents = AgentManager(t_s, w_prev, h_prev, offset, directions, exit_points, maze, direct)
agents.add_new([1, 1], random.randint(0, 360), [.0, .0, .6])
# agents.add_new([1, 0], random.randint(0, 360), [.0, .0, .6])
# agents.add_new([2, 0], random.randint(0, 360), [.0, .0, .6])
# agents.add_new([3, 3], random.randint(0, 360), [.0, .0, .6])
# agents.add_new([4, 0], random.randint(0, 360), [.0, .0, .6])
agents.add_new([15, 5], random.randint(0, 360), [.0, .0, .6])
agents.add_new([90, 70], random.randint(0, 360), [.0, .0, .6])


def mouse_button_callback(window, button, action, mods):
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        pos_x, pos_y = glfw.get_cursor_pos(window)
        pos_x -= offset
        pos_y -= offset
        pos = [-1, -1]
        for it in range(len(maze)):
            if t_s[1] * it < pos_y < t_s[1] * (it + 1):
                pos[0] = it
        for it in range(len(maze[0])):
            if t_s[0] * it < pos_x < t_s[0] * (it + 1):
                pos[1] = it
        if pos[0] != -1 and pos[1] != -1 and maze[pos[0]][pos[1]] != 1:
            agents.add_new(pos, 33.0, [.0, .0, .9])


def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_LEFT and action == glfw.REPEAT:
        camera_position[0] -= 10
    if key == glfw.KEY_RIGHT and action == glfw.REPEAT:
        camera_position[0] += 10

    if key == glfw.KEY_DOWN and action == glfw.REPEAT:
        camera_position[1] -= 10
    if key == glfw.KEY_UP and action == glfw.REPEAT:
        camera_position[1] += 10


glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_key_callback(window, key_callback)

old_step_time = glfw.get_time()
previous_time = glfw.get_time()
frame_count = 0
while not glfw.window_should_close(window):

    current_time = glfw.get_time()
    frame_count += 1

    # if current_time - old_step_time >= 0.1:
    agents.step()
    # old_step_time = current_time

    if current_time - previous_time >= 1.0:
        glfw.set_window_title(window, "Modelowanie i Symulacja Systemów - Symulacja (" + str(frame_count) + " FPS)")
        frame_count = 0
        previous_time = current_time

    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    w, h = glfw.get_window_size(window)
    glViewport(0, 0, w, h)

    if w != w_prev and h != h_prev:
        w_prev = w
        h_prev = h
        t_s[0] = (w - 2 * (offset + 1)) / len(maze[0])
        t_s[1] = (h - 2 * (offset + 1)) / len(maze)
        agents.set_client_tile_size(w, h, t_s)

    glOrtho(0, w, 0, h, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(camera_position[0], camera_position[1], camera_position[2])

    # draw outline
    glColor3ub(255, 0, 0)
    glBegin(GL_LINE_LOOP)

    glVertex2f(0 + offset, 0 + offset)
    glVertex2f(0 + offset, h - offset)
    glVertex2f(w - offset, h - offset)
    glVertex2f(w - offset, 0 + offset)

    glEnd()


    # draw tile [n, m]
    def draw_tile(n, m, block_type, draw_debug):

        if block_type == 0:
            glColor3ub(free_color[0], free_color[1], free_color[2])
        else:
            glColor3ub(collision_color[0], collision_color[1], collision_color[2])

        o = offset + 1

        glBegin(GL_TRIANGLES)

        glVertex2f(0 + o + (m * t_s[0]), h - o - (n * t_s[1]))
        glVertex2f(0 + o + (m * t_s[0]), h - o - (n * t_s[1]) - t_s[1])
        glVertex2f(0 + o + (m * t_s[0]) + t_s[0], h - o - (n * t_s[1]))

        glVertex2f(0 + o + (m * t_s[0]) + t_s[0], h - o - (n * t_s[1]))
        glVertex2f(0 + o + (m * t_s[0]), h - o - (n * t_s[1]) - t_s[1])
        glVertex2f(0 + o + (m * t_s[0]) + t_s[0], h - o - (n * t_s[1]) - t_s[1])

        glEnd()

        if draw_debug:
            glColor3ub(60, 60, 60)
            glBegin(GL_LINE_LOOP)

            glVertex2f(0 + o + (m * t_s[0]), h - o - (n * t_s[1]))
            glVertex2f(0 + o + (m * t_s[0]), h - o - (n * t_s[1]) - t_s[1])
            glVertex2f(0 + o + (m * t_s[0]) + t_s[0], h - o - (n * t_s[1]) - t_s[1])
            glVertex2f(0 + o + (m * t_s[0]) + t_s[0], h - o - (n * t_s[1]))

            glEnd()


    # draw map
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            draw_tile(i, j, maze[i][j], False)  # True for helper lines

    # draw agents
    agents.draw_all()

    glfw.swap_buffers(window)

glfw.terminate()
