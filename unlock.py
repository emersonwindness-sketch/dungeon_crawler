#Unlocked access and overall progress | 0 means unlocked, 1 locked.

from inventory import *
from trade import *

def safe_room_tavern(source, world, current_room):
    if "Room key" in source:
        world.update({"Tavern":{"description": "A familiar place, you paid your room here, enjoy it while you can.", "choice": ["Road", "Room"]}})
        world.update({"Room": {"description": "Your room for the forseeable future, not much, but it will suffice, a Chest for your items and a bed for some rest.", "choice": ["Chest", "Tavern"]}})
        current_room = "Room"
        return
        
    elif "Room key" not in source:
        print ("You don't have the key.")



