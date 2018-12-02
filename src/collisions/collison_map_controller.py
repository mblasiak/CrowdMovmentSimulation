# Mark fileds on collision_map by adding to them given value
# Ignores marking out of map boundries

def mark_location_as_taken(self, location, collision_map, marking_value):
    location_x, location_y = location
    if location_x < 0 or location_x > len(collision_map):
        return False
    if location_y < 0 or location_y > len(collision_map[0]):
        return False
    collision_map[location_x, location_y] = collision_map[location_x][location_x] + marking_value
    return True
