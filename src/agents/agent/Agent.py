class Agent:

    def __init__(self, start_position , end_postion, max_step, front_collison_size, rear_collision_size, directions_map,
                 collision_map):

        self.start = start_position
        self.end = end_postion
        self.current_pos = self.start
        self.max_step = max_step

        self.front_collision_size = front_collison_size
        self.rear_collision_size = rear_collision_size
        self.direction_map = directions_map
        self.collision_map = collision_map
        self.map_x_size = len(directions_map)
        self.map_y_size = len(directions_map[0])

    def get_available_moves(self):
        pass

    def get_move_price(self):
        pass

    def get_best_move(self):
        pass

    def update_collision_map(self):


        pass

    def clear_position_to_collision_map(self):
        pass

    def add_position_to_collision_map(self):
        pass

    def move(self):
        pass

    def check_reached_finish(self):

        if self.end == self.current_pos:
            return True
        else:
            return False
