print ("Welcome to the depricated, dark and dead world after the awakening")
print ("------------------------------------------------------------------")
print ("Walking for days, hiding in the shadows, avoiding anything and everyone, after all, you don't really know who is what they claim to be, well, not after the falling\nType 'inventory' to access it.\n")

from inventory import *
from unlock import *
from trade import *
from engine import *
from mechanics.maps.all_maps import *

# -- Starting Area -- #

current_map = road
print (f"{current_map.description}\n Exits: {current_map.access}")

# -- Main Gameplay Loop -- #

while True:

    player_choice = input(f"\nwhat would you like to do?: ").capitalize()
    current_map = world_access_check(player_choice, current_map, world_registry)

# -- Container Interaction -- #
    
    if current_map.has_container is True:
        print (f"This place has a container named '{current_map.container_name}'\nType 'container' if you want to interact with it: ")
        
    if player_choice == "Container" and current_map.has_container is True:
        container_overview(Inventory)
        container_overview(Chest)
        container_interaction(Inventory)

# -- Inventory -- #
    
    if player_choice == "Inventory":
        container_overview(Inventory)

# -- Trade -- #

            

        
        



        

        









       


    