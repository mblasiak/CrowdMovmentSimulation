from src.agent.Agent import Agent
from src.direction_map.DirectionMap import DirectionMap
from src.environment.environment import direction_map
from src.environment.line import Point

star_pos = (1, 1)
end_pos = (99, 99)

collisions = [[0] * 100] * 100
collisions[10][10] = 1
collisions[11][10] = 1

collisions[1][11]=1
collisions[1][12]=1

print("Mapa colizji: {}".format(collisions))


directions = direction_map(collisions, [Point(7, 7)], 3)
print(directions)




# direct = DirectionMap(directions)
# human_0 = Agent(star_pos, end_pos, 3, 3, 2, direct, collisions)
# human_0.move()
# human_0.move()
# human_0.move()
# human_0.move()
# human_0.move()
# human_0.move()
# human_0.move()
# human_0.move()
