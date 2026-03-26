def world_access_check(player_choice, current_map, world_registry):
    if player_choice in current_map.access:
        print ("yep that place does existe yea")
        current_map = world_registry[player_choice]
        print (current_map.access)
        return current_map
    else:
        print ("Cant access this place")
        return current_map

def display_map(player_choice, map):
    pass