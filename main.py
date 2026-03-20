print ("Welcome to the depricated, dark and dead world after the awakening")
print ("------------------------------------------------------------------")
print ("Walking for days, hiding in the shadows, avoiding anything and everyone, after all, you don't really know who is what they claim to be, well, not after the falling")
print ("you've been walking for too long, the only options would be the Tavern to the east of here, or the forest to the north.")

world = {

    "Road":{
        "description": "The road, you've been walking for too long, the only options would be the Tavern to the east of here, or the Forest to the north.",
        "choice": ["Forest", "Tavern"]
    },

    "Tavern":{
        "description": "You enter the Tavern, a comfortable place to stay the night, that is, if you have the money to pay?",
        "choice": ["Room", "Road"]
    },

    "Forest":{
        "description": "You keep walking towards the forest, however, it is eerie quiet... something isnt right.",
        "choice": ["Cave", "North", "Road"]
    },

    "Unlockedroom":{
        "description": "You rent a room, costing all the gold you took with you in your jorney, atleast, some rest for the night before continuing",
        "choice": ["placeholder", "placeholder"]
    }, 
}

Inventory = {
    
    "Bag":{
        "Gold":{"Value": 50
        },
        "Dagger":{"Value": 1
        },
        "HP Potion": {"Value": 3
        },
    }
}


def display_room(player_choice):

    player_choice = world[player_choice]
    print (player_choice["description"])
    choices = ", " .join(player_choice["choice"])
    print (f"exits: {choices}")


def access_inventory(access):
    access = ", " .join(Inventory["Bag"])
    print (access)
    #Place holder for modifying inventory.
    
overview = ", " .join(Inventory["Bag"])

def combat():
    pass
 

current_room = "Road"
alive = True
counter = 0
print ("Type Inventory to acess it.")

while alive is True:
    
    player_choice = input(f"what would you like to do? ").capitalize()
    print (f"You choose to: {player_choice}")
    if player_choice in world:
        current_room = player_choice
        display_room(current_room)
    
    if player_choice == "Room":
        print ("Got the money to pay, stranger?")

    elif player_choice not in world and player_choice != "Inventory":
        print ("Cannot go there!")
        counter += 1
        if counter >= 3:
            print ("You wander aimlessly towards the world, your luck eventually ran out, something got you, and no one ever heard from you again\nYou DIED")
            alive = False

# - INVENTORY SECTION - #

    if player_choice == "Inventory":

        print (overview)

        inv_open = True
        while inv_open is True:

            inv_open = input("Type 'Exit' to leave.\nType 'Modify' to discart or add items you found\n").capitalize()
            if inv_open == "Exit":
                inv_open = False

            elif inv_open == "Modify":
                access = input("What you want to see?\n").capitalize()
                
                if access in Inventory["Bag"]:
                    show = Inventory["Bag"][access]["Value"]
                    print (f"You have {show} {access}")

                else:
                    print ("You dont have this item")
                    inv_open = True

            else:
                print ("Modify to manipulate inventory or 'Exit' to leave.")
                inv_open = True








       


    