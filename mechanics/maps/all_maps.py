# -- Instructions on how to create maps.

class Map:
    def __init__(self, name, description, access, has_container, container_name, has_trader, trader_name, is_locked):
        self.name = name
        self.description = description
        self.access = access
        self.has_container = has_container
        self.container_name = container_name
        self.has_trader = has_trader
        self.trader_name = trader_name
        self.is_locked = is_locked

road = Map("Road",
           "The road, you've been walking for too long, the only options would be the Tavern to the east of here, or the Forest to the north.",
           ["Tavern", "Forest"],
           False,
           "NoContainer",
           False,
           "NoNPC",
           False
          )

tavern = Map("Tavern",
             "You enter the Tavern, a comfortable place to stay the night, that is, if you have the money to pay?", 
            ["Room", "Road"],
            False,
            "None",
            True,
            "Dan",
            False    
            )

room = Map("Room",
           "Your own room, for now, you paid a decent chunk of gold, but atleast you'll have some comfort, a chest and a bed.",
           ["Tavern"],
           True,
           "Chest",
           False,
           "NoNPC",
           True
            )

forest = Map ("Forest",
            "Entering the forest, you feel a weird sensation, fear perhaps? caution? anxiety? you can't tell, but the feeling of being watched is strong here.",
            ["Cave", "Road"],
            False,
            "NoContainer",
            False,
            "NoNPC",
            False
            )

cave = Map("Cave",
           "Too dark too see, you will need some kind of light to go any further",
           ["Forest"],
           False,
           "NoContainer",
           False,
           "NoNPC",
           False
           )

class Chest:
    def __init__(self, name, contents):
        self.name
        self.contents

room_chest = Chest("Room Chest",
                   )

#-- World Registry --#

#Everytime a new map is added, please, put its name then the object itself, so the program can actually read it.

world_registry = { 

        "Road": road,
        "Forest": forest,
        "Tavern": tavern,
        "Room": room,
        "Cave": cave

}