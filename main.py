print ("Welcome to the depricated, dark and dead world after the awakening")
print ("------------------------------------------------------------------")
print ("Walking for days, hiding in the shadows, avoiding anything and everyone, after all, you don't really know who is what they claim to be, well, not after the falling")
print ("you've been walking for too long, the only options would be the Tavern to the east of here, or the forest to the north.")

from inventory import *
from unlock import *
from trade import *

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
        "choice": ["Chest", "Tavern"]
    },
    "Cavern": {
        "description": "In the midst of the darkness, you see something in the corner of a dark cave room, looks like someone, or, looked like someone one day\nNothing but a corpse, the problem lies in the fact that it doesn't look very rotten, it happened recently...",
        "choice": ["Corpse Inventory", "Forest"]
    }
}

def display_room(player_choice):
    player_choice = world[player_choice]
    print (player_choice["description"])
    choices = ", " .join(player_choice["choice"])
    print (f"Exits: {choices}")
       
current_room = "Road"
deathcounter = 0
print ("Type Inventory to acess it.")
alive = True

while alive is True:
       
    player_choice = input(f"\nwhat would you like to do? ").capitalize()
    print (f"You choose to: {player_choice}")
    if player_choice in world:
            current_room = player_choice
            display_room(current_room)
        
    if player_choice == "Room":
            if tavern_room == 1:
                 print ("You already paid, you can go straight to your room, don't forget our costumer services!")
                 print ("Exits: Chest, Tavern")
            elif tavern_room == 0:
                print ("Got the money to pay, stranger? it costs 50 gold.")
                choice = input("Will you pay the gold? Y/N ").capitalize()
                if choice == "Y":
                    if Inventory["Gold"] >= 50:
                        Inventory["Gold"] -= 50
                        print ("Pleasure doing business.")
                        display_room("Unlockedroom")
                        tavern_room = 1
                    else:
                        print ("Not enough money, get out of here.")
                elif choice == "N":
                    print ("Well, get out of here then.")

    elif player_choice not in world and player_choice != "Inventory":
            print ("Cannot go there!")
            deathcounter += 1
            if deathcounter >= 3:
                print ("You wander aimlessly towards the world, your luck eventually ran out, something got you, and no one ever heard from you again\nYou DIED")
                alive = False

    # - INVENTORY SECTION - #

    if player_choice == "Inventory":

        item_overview(Inventory)

        if current_room == "Room":            
            inv_open = True

            while inv_open is True:
                inv_open = input("Type 'Exit' to leave.\nType 'Modify' to discart or add items you found\n").capitalize()

                if inv_open == "Exit":
                    inv_open = False

                elif inv_open == "Modify":
                    source = input("You want to move your inventory or take from chest?\nMove / Take: ").capitalize()
                    item_name = input("What item?\n").capitalize()
                    num_item = int(input("How many?\n"))

                    if source == "Move":
                        source = Inventory
                        destination = Chest
                        transfer_items(source, destination, item_name, num_item)
                        item_overview(Inventory)
                        item_overview(Chest)

                    elif source == "Take":
                        source = Chest
                        destination = Inventory
                        transfer_items(source, destination, item_name, num_item)
                        item_overview(Inventory)
                        item_overview(Chest)

                else:
                    print ("Modify to manipulate inventory or 'Exit' to leave.")
                    inv_open = True
        else: 
            print ("\nNo chest or loot nerby to interact.")








       


    