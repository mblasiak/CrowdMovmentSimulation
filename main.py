import glfw
from OpenGL.GL import *

from gfx.MazeTexture import MazeTexture
from model.direction_map.DirectionMap import DirectionMap
from model.environment.line import Point
from gfx.AgentManager import AgentManager
from resources.handling.reading import load_direction_from_file, load_map_from_file
from random import randint

if not glfw.init():
    exit(1)

# global intensity
global global_intensity

global_intensity = 50

window = glfw.create_window(1280, 720, "Modelowanie i Symulacja Systemów - Symulacja (0 FPS)", None, None)
glfw.make_context_current(window)

simulation_running = True

if not window:
    glfw.terminate()
    exit(1)

map_filename = "resources/ready/galeria_krakowska_maze100x100.txt"

maze_original = load_map_from_file(map_filename)
maze = load_map_from_file(map_filename)

exit_points = []
for i in range(40, 60):
    exit_points.append(Point(99, i))

# directions = direction_map(maze, exit_points, 1)
directions_1 = load_direction_from_file("resources/ready/GK_directionmap_one_100x100.txt")
directions_2 = load_direction_from_file("resources/ready/GK_directionmap_two_100x100.txt")
directions_3 = load_direction_from_file("resources/ready/GK_directionmap_three_100x100.txt")
directions_4 = load_direction_from_file("resources/ready/GK_directionmap_four_100x100.txt")

direct = [DirectionMap(directions_1), DirectionMap(directions_2), DirectionMap(directions_3),
          DirectionMap(directions_4)]

w_prev = 1280
h_prev = 720

offset = 20

tile_size = [(w_prev - 2 * (offset + 1)) / len(maze[0]), (h_prev - 2 * (offset + 1)) / len(maze)]

agents = AgentManager(tile_size, w_prev, h_prev, offset, exit_points, maze, direct)

mazeTexture = MazeTexture(maze_original, w_prev, h_prev, offset, tile_size)


def mouse_button_callback(window, button, action, mods):
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        pos_x, pos_y = glfw.get_cursor_pos(window)
        pos_x -= offset
        pos_y -= offset
        pos = [-1, -1]
        for it in range(len(maze)):
            if tile_size[1] * it < pos_y < tile_size[1] * (it + 1):
                pos[0] = it
        for it in range(len(maze[0])):
            if tile_size[0] * it < pos_x < tile_size[0] * (it + 1):
                pos[1] = it
        if pos[0] != -1 and pos[1] != -1 and maze[pos[0]][pos[1]] != 1:
            agents.add_new(pos, 33.0, [.0, .0, .9], 0)


def key_callback(window, key, scancode, action, mods):
    global global_intensity
    if key == glfw.KEY_KP_ADD and action == glfw.RELEASE:
        global_intensity += 10
        if global_intensity > 100:
            global_intensity = 100
    if key == glfw.KEY_KP_SUBTRACT and action == glfw.RELEASE:
        global_intensity -= 10
        if global_intensity < 0:
            global_intensity = 0
    if key == glfw.KEY_KP_ADD and action == glfw.RELEASE:
        print("Wcisnalem!")
    if key == glfw.KEY_SPACE and action == glfw.PRESS:
        global simulation_running
        simulation_running = not (simulation_running and True)


glfw.set_mouse_button_callback(window, mouse_button_callback)
glfw.set_key_callback(window, key_callback)

old_step_time = glfw.get_time()
previous_time = glfw.get_time()
frame_count = 0

while not glfw.window_should_close(window):

    current_time = glfw.get_time()
    frame_count += 1

    if simulation_running:
        agents.step()

    if current_time - previous_time >= 1.0:
        title = "Crowd Simulation ( " + str(frame_count) + " FPS | Number Of Agents: " + str(
            len(agents.agent_list)) + " )" + " intensity: " + str(global_intensity)
        glfw.set_window_title(window, title)
        frame_count = 0
        previous_time = current_time

    glfw.poll_events()

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    w, h = glfw.get_window_size(window)

    if w != w_prev or h != h_prev:
        w_prev = w
        h_prev = h
        tile_size[0] = (w - 2 * (offset + 1)) / len(maze[0])
        tile_size[1] = (h - 2 * (offset + 1)) / len(maze)
        agents.set_client_tile_size(w, h, tile_size)
        mazeTexture.reconstruct(w, h, tile_size)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, 0, h, -10, 10)

    glMatrixMode(GL_MODELVIEW)

    mazeTexture.draw()

    agents.draw_all()

    glfw.swap_buffers(window)

    intensity = randint(0, 100)
    if intensity < global_intensity:
        pos = [randint(50, 99), 98]
        which_map = randint(0, 1)
        agents.add_new(pos, 33.0, [.0, .0, .9], which_map)

        pos = [randint(2, 90), 2]
        which_map = randint(2, 3)
        agents.add_new(pos, 33.0, [.0, .0, .9], which_map)

mazeTexture.release()
glfw.terminate()
