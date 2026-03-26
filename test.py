from inventory import *
from unlock import *
from trade import *
from mechanics.engine import *
from mechanics.maps.tavern import *
from mechanics.maps.road import *

world_registry = { 
        "Road": road,
        "Tavern": tavern,
}

#starting area

current_map = road

#------------

while True: 
    player_choice = input(f"\nwhat would you like to do? ").capitalize()
    current_map = world_access_check(player_choice, current_map, world_registry)
    



