import copy

from gfx.AgentGfx import AgentGfx
from model.agent.Agent import ExitReached


class AgentManager:
    def __init__(self, initial_tile_size: [float, float], client_width: int, client_height: int, map_offset: int,
                 exit, maze, direct):
        self.agent_list = list()
        self.tile_size = initial_tile_size
        self.agent_radius = (initial_tile_size[1] - initial_tile_size[1] / 5) / 2
        self.width = client_width
        self.height = client_height
        self.offset = map_offset
        self.exit_points = exit
        self.maze = maze
        self.maze_for_agent=copy.deepcopy(maze)
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

    def add_new(self, position: [int, int], angle: float, color: [float, float, float], which_map):

        correct_pos = [
            0 + self.offset + 1 + (position[1] * self.tile_size[0]) + (self.tile_size[0] / 2),
            self.height - self.offset - 1 - (position[0] * self.tile_size[1]) - (self.tile_size[1] / 2)
        ]

        if self.maze_for_agent[position[0]][position[1]] == 0:
            self.agent_list.append(AgentGfx(correct_pos, position, angle, color, self.maze_for_agent, self.direct, which_map))
        else:
            print('Agent can not be adde on this pos')

    def step(self):
        moving_lsit = sorted(self.agent_list, key=lambda agt: agt.agent.anger, reverse=True)

        any_moved = True

        while any_moved:
            any_moved = False

            for agent in moving_lsit:
                try:
                    anger = agent.move()
                except ExitReached:
                    self.agent_list.remove(agent)
                    moving_lsit.remove(agent)

                else:
                    if anger == 0:
                        any_moved = True
                        moving_lsit.remove(agent)

                        agent.map_position = agent.agent.current_pos
                        agent.fx_pos = [
                            0 + self.offset + 1 + (agent.map_position[1] * self.tile_size[0]) + (self.tile_size[0] / 2),
                            self.height - self.offset - 1 - (agent.map_position[0] * self.tile_size[1]) - (
                                    self.tile_size[1] / 2)
                        ]

                        agent.position = agent.fx_pos
