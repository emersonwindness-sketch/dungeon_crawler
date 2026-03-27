from mechanics.maps.data import map, npc

#

#--Road--#

road = map("Road",
           "The road, you've been walking for too long, the only options would be the Tavern to the east of here, or the Forest to the north.",
           ["Tavern", "Forest"],
           False,
           "None"
          )

#--Tavern--#

tavern = map("Tavern",
             "You enter the Tavern, a comfortable place to stay the night, that is, if you have the money to pay?", 
            ["Room", "Road"],
            False,
            "None"
             )

bartender = npc("Bartender",
                "Hello there mate, looking to stay? the room will cost you 50 gold.",
             )

#--Room--#

room = map("Room",
           "Your own room, for now, you paid a decent chunk of gold, but atleast you'll have some comfort, a chest and a bed.",
           ["Tavern"],
           True,
           "Chest"
            )

#--Forest--#

forest = map ("Forest",
            "Entering the forest, you feel a weird sensation, fear perhaps? caution? anxiety? you can't tell, but the feeling of being watched is strong here.",
            ["Cave", "Road"],
            False,
            "None"
            )

#--Cave--#

cave = map("Cave",
           "Too dark too see, you will need some kind of light to go any further",
           ["Forest"],
           False,
           "None"
           )

#--World Registry--#

#Everytime a new map is added, please, put them in here so the program can actually read the map.

world_registry = { 
        "Road": road,
        "Forest": forest,
        "Tavern": tavern,
        "Room": room,
        "Cave": cave
}