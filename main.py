print ("Welcome to the depricated, dark and dead world after the awakening")

world = {
    "Road":{
        "description": "A comfortable place to stay in the night, you walked days to get here, hiding in the shadows, avoiding anything and everyone, after all, you don't really know who is what they claim to be, well, not after the falling.",
        "choice": ["Forest", "Tavern"]
    },
    "Tavern":{
        "description": " Description here for the Tavern ",
        "choice": ["Room", "Road"]
    },
    "Forest":{
        "description": " Description here for the Forest ",
        "choice": ["Cave", "South", "Road"]
    },
       
}

def display_room(room):

    room_data = world[room]
    print (room_data)
    
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
        player_choice not in world
        print ("Cannot go there!")
        counter += 1
        if counter >= 3:
            print ("You wander aimessly towards the world, your luck eventually ran out, something got you, and no one ever heard from you again")
            print ("YOU DIED")
            alive = False
       


    
