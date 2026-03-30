from inventory import *


def world_access_check(player_choice, current_map, world_registry):

    if player_choice in current_map.access:
        current_map = world_registry[player_choice]
        print (f"{current_map.description}\n Exits: {current_map.access}\n")
        return current_map
    
    else:
        return current_map

def display_map(player_choice, map):
    pass