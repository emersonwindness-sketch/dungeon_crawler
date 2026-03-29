from mechanics.maps.all_maps import *
from mechanics.maps.all_items import *
from mechanics.maps.data import *

Inventory = starting_player_items

Chest = {}



def transfer_items(source, destination, item_name, num_item):
    try:
        
        item = source[item_name]
        name = item.name

    except KeyError:
        print ("Item not found")
        return
    
    if source[item_name].quantity < num_item:
        print (f"You only have {item.quantity} of those.")
        return

    if name not in destination:
        destination[item_name] = item.copy(0)

    destination[item_name].quantity += num_item
    source[item_name].quantity -= num_item

    if source[item.name].quantity <=0:
        del source[item_name]

    container_overview(Inventory)        
    container_overview(Chest)

def container_overview(source):

    if source == Inventory:
        print ("\n----Inventory----\n")

    elif source == Chest:
        print ("\n------Chest------\n")

    for x in source:
        item_obj = source[x]
        
        name = item_obj.name
        weight = item_obj.weight * item_obj.quantity
        value = item_obj.value * item_obj.quantity
        quantity = item_obj.quantity

        overview = f"{name}: {value}g | {weight} kg | {quantity} copy's."
        print (overview)

def container_interaction(Inventory):
            
    inv_open = True

    player_choice = input("\n----To exit inventory, type 'Exit'----\nYou want to store or take items?\n 'Take' or 'Store': ").capitalize()
 
    while inv_open is True:       
        if player_choice == "Take":
            try: 
                item_name = input("What item do you want to move?: ").capitalize()
                num_item = int(input("How many?: "))
                transfer_items(Chest, Inventory, item_name, num_item)
            except ValueError:
                print ("Please, use only numbers for the quantity of items.")

        if player_choice == "Store":
            try: 
                item_name = input("What item do you want to move?: ").capitalize()
                num_item = int(input("How many?: "))
                transfer_items(Inventory, Chest, item_name, num_item)
            except ValueError:
                print ("Please, use only numbers for the quantity of items.")

        if player_choice == "Exit":
            inv_open = False
        
        else:
            player_choice = input("Choose one of them: 'Take' | Store | Exit : ").capitalize()