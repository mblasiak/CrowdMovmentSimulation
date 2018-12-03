from src.agent.Agent import Agent
from src.direction_map.DirectionMap import DirectionMap
from src.environment.environment import map_environment
star_pos=(0,0)
end_pos=(99,99)
collisions=[[0]*10]*10
directions=map_environment(collisions,end_pos)



print(collisions)


