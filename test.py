from inventory import *
from unlock import *
from trade import *
from mechanics.engine import *
from mechanics.maps.all_maps import *

#starting area

current_map = road

#------------

while True: 
    player_choice = input(f"\nwhat would you like to do? ").capitalize()
    current_map = world_access_check(player_choice, current_map, world_registry)
    print (f"does this place has a chest?\n{current_map.has_chest}")
           
    



