print ("Welcome to the depricated, dark and dead world after the awakening")
print ("------------------------------------------------------------------")
print ("Walking for days, hiding in the shadows, avoiding anything and everyone, after all, you don't really know who is what they claim to be, well, not after the falling\nType 'inventory' to access it.\n")

from inventory import *
from unlock import *
from trade import *
from mechanics.engine import *
from mechanics.maps.all_maps import *

# -- Starting Area -- #

current_map = road
print (f"{current_map.description}\n Exits: {current_map.access}")

# -- Main Gameplay Loop -- #

while True:

    player_choice = input(f"\nwhat would you like to do? ").capitalize()
    current_map = world_access_check(player_choice, current_map, world_registry)
    
    if current_map.has_container is True:
        player_choice = input(f"This place has a container named '{current_map.container_name}'\nType 'container' to interact with it\n").capitalize()
        
        if player_choice == "Container":
            container_overview(Inventory)
            container_interaction(Inventory)

        else:
            current_map = world_access_check(player_choice, current_map, world_registry)
            print (f"{current_map.description}\n{current_map.access}")

# -- Inventory -- #
    
    if player_choice == "Inventory":
        container_overview(Inventory)

            

            
        


            



        

        









       


    