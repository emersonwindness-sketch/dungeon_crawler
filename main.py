print ("Welcome to the depricated, dark and dead world after the awakening")
print ("------------------------------------------------------------------")
print ("Walking for days, hiding in the shadows, avoiding anything and everyone, after all, you don't really know who is what they claim to be, well, not after the falling")
print ("you've been walking for too long, the only options would be the Tavern to the east of here, or the forest to the north.")

world = {
    "Road":{
        "description": "The road, you've been walking for too long, the only options would be the Tavern to the east of here, or the forest to the north.",
        "choice": ["Forest", "Tavern"]
    },
    "Tavern":{
        "description": "Description here for the Tavern ",
        "choice": ["Room", "Road"]
    },
    "Forest":{
        "description": "Description here for the Forest ",
        "choice": ["Cave", "North", "Road"]
    },
       
}

def display_room(player_choice):

    player_choice = world[player_choice]
    print (player_choice["description"])
    choices = ", " .join(player_choice["choice"])
    print (f"exits: {choices}")

    
current_room = "Road"
alive = True
counter = 0

while alive is True:
    
    player_choice = input(f"what would you like to do? ").capitalize()
    print (f"you choose to: {player_choice}")
    if player_choice in world:
        current_room = player_choice
        display_room(current_room)

    else: 
        print ("Cannot go there!")
        counter += 1
        if counter >= 3:
            print ("You wander aimlessly towards the world, your luck eventually ran out, something got you, and no one ever heard from you again\nYou DIED")
            alive = False
       


    