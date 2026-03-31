print ("Welcome to the depricated, dark and dead world after the awakening")
print ("------------------------------------------------------------------")
print ("Walking for days, hiding in the shadows, avoiding anything and everyone, after all, you don't really know who is what they claim to be, well, not after the falling\nType 'inventory' to access it.\n")

from inventory import *
from unlock import *
from trade import *
from engine import *
from mechanics.maps.all_maps import *
from mechanics.player_stats import *

from os import system
system("clear||cls")

# -- Choose Player Class -- #

player_class = traveler

# -- Starting Area -- #

current_map = road
print (f"{current_map.description}\n Exits: {current_map.access}")

# -- Main Gameplay Loop -- #

while True:

    player_choice = input(f"\nwhat would you like to do?: \n").capitalize()
    current_map = world_access_check(player_choice, current_map, world_registry)

# -- Container Interaction -- #
    
    if current_map.has_container is True:
        print (f"This place has a container named '{current_map.container_name}'\nType 'container' if you want to interact with it\nOr 'show' to se its contents: \n")
        
    if current_map.has_container is True and player_choice == "Container":
        container_interaction()
        
    if current_map.has_container is True and player_choice == "Show":
        container_overview(Chest, current_map.container_name)

    elif current_map.has_container is False and player_choice == "Container":
        print ("No container in this map.\n")    

# -- Inventory -- #
    
    if player_choice == "Inventory":
        container_overview(Inventory, "Inventory")

# -- Trade -- #

    if current_map.has_trader is True:
        print ("There's a trader here, type 'Trade' to see his inventory.")

    if current_map.has_trader is True and player_choice =="Trade":
        trade(Inventory, trader_inventory)
                 
 # -- Unlocking -- # 


        
        


        

        









       


    