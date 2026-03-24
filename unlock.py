#Unlocked access and overall progress | 0 means unlocked, 1 locked.

from inventory import *

def safe_room_tavern(source, world):
    if "Room key" in source:
        print ("You enter your safe room.\nYour room for the forseeable future, not much, but it will suffice, a Chest for your items and a bed for some rest.")
        world.update({"Tavern":{"description": "A familiar place, you paid your room here, enjoy it while you can.", "choice": ["Road", "Room"]}})
        return
        
    elif "Room key" not in source:
        print ("You don't have the key.")
        room = "Road"



