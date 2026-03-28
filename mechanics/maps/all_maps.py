from mechanics.maps.data import Map, Npc

#-- Road --#

road = Map("Road",
           "The road, you've been walking for too long, the only options would be the Tavern to the east of here, or the Forest to the north.",
           ["Tavern", "Forest"],
           False,
           "NoContainer",
           False,
           "NoNPC"
          )

#-- Tavern --#

tavern = Map("Tavern",
             "You enter the Tavern, a comfortable place to stay the night, that is, if you have the money to pay?", 
            ["Room", "Road"],
            False,
            "None",
            True,
            "Dan",
             )

bartender = Npc("Bartender",
                "Hello there mate, looking to stay? the room will cost you 50 gold.",
             )

#-- Room --#

room = Map("Room",
           "Your own room, for now, you paid a decent chunk of gold, but atleast you'll have some comfort, a chest and a bed.",
           ["Tavern"],
           True,
           "Chest",
           False,
           "NoNPC"
            )

#-- Forest --#

forest = Map ("Forest",
            "Entering the forest, you feel a weird sensation, fear perhaps? caution? anxiety? you can't tell, but the feeling of being watched is strong here.",
            ["Cave", "Road"],
            False,
            "NoContainer",
            False,
            "NoNPC"
            )

#-- Cave --#

cave = Map("Cave",
           "Too dark too see, you will need some kind of light to go any further",
           ["Forest"],
           False,
           "NoContainer",
           False,
           "NoNPC"
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