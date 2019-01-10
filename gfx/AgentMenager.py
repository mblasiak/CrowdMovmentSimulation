from gfx.AgentGfx import AgentGfx


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

        # dir_x, dir_y = self.direction_map[position[0]][position[1]]

        self.agent_list.append(AgentGfx(correct_pos, position, angle, color, self.maze, self.direct))

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
