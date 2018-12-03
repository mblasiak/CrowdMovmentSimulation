# Mark fileds on collision_map by adding to them given value
# Ignores marking out of map boundries
import src.navigator.navigator as nav


def mark_location_as_taken(location: (int,int), collision_map, marking_value:int):
    location_x, location_y = location
    if location_x < 0 or location_x > len(collision_map):
        return False
    if location_y < 0 or location_y > len(collision_map[0]):
        return False
    collision_map[location_x, location_y] = collision_map[location_x][location_x] + marking_value
    return True


def add_circle_obstacle(center_location: (int,int), radius: int, collision_map: int[[]], marking_value:int):
    (loc_x, loc_y) = center_location
    for x in range(loc_x - radius, loc_x + radius):
        for y in range(loc_y - radius, loc_y + radius):
            distance = nav.get_distance_beteween_points(center_location, (x, y))
            if distance <= radius:
                mark_location_as_taken((x, y), collision_map, marking_value)


def add_squere_obstacle(center_location: (int,int), border_lenght: int , collision_map: int[[]], marking_value: int):
    (loc_x, loc_y) = center_location
    for x in range(loc_x - border_lenght / 2, loc_x + border_lenght / 2):
        for y in range(loc_y - border_lenght / 2, loc_y + border_lenght / 2):
            mark_location_as_taken((x, y), collision_map, marking_value)
