# Mark fileds on collision_map by adding to them given value
# Ignores marking out of map boundries
import src.agents.navigation.navigator.navigator as nav


def mark_location_as_taken(location, collision_map, marking_value):
    location_x, location_y = location
    if location_x < 0 or location_x > len(collision_map):
        return False
    if location_y < 0 or location_y > len(collision_map[0]):
        return False
    collision_map[location_x, location_y] = collision_map[location_x][location_x] + marking_value
    return True


def add_circle_obstacle(center_location, radious, collision_map, marking_value):
    (loc_x, loc_y) = center_location
    for x in range(loc_x - radious, loc_x + radious):
        for y in range(loc_y - radious, loc_y + radious):
            distance = nav.get_distance_beteween_points(center_location, (x, y))
            if distance <= radious:
                mark_location_as_taken((x, y), collision_map, marking_value)


def add_squere_obstacle(center_location, border_lenght, collision_map, marking_value):
    (loc_x, loc_y) = center_location
    for x in range(loc_x - border_lenght / 2, loc_x + border_lenght / 2):
        for y in range(loc_y - border_lenght / 2, loc_y + border_lenght / 2):
            mark_location_as_taken((x, y), collision_map, marking_value)
