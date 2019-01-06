import glfw
from OpenGL.GL import *
import random


from model.direction_map.DirectionMap import DirectionMap
from model.environment.line import Point
from gfx.AgentMenager import AgentManager
from resources.handling.reading import load_direction_from_file,load_map_from_file




if not glfw.init():
    exit(1)

window = glfw.create_window(1280, 720, "Modelowanie i Symulacja Systemów - Symulacja (0 FPS)", None, None)
glfw.make_context_current(window)

if not window:
    glfw.terminate()
    exit(1)

camera_position = [0.5, 0.5, 0]

maze = load_map_from_file("resources/ready/dobry_maze100na100.txt")

exit_points = []
for i in range(40, 60):
    exit_points.append(Point(99, i))

# directions = direction_map(maze, exit_points, 1)
directions = load_direction_from_file("resources/ready/directios100x100yx.txt")
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
