from mechanics.maps.all_maps import *
from mechanics.maps.all_items import *
from engine import *

Inventory = starting_player_items

Chest = {}

tavern_trader = trader_inventory

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
        destination[name] = item.copy(0)

    destination[item_name].quantity += num_item
    source[item_name].quantity -= num_item

    if source[item_name].quantity <=0:
        del source[name]

def container_overview(source, name):

    print (f"-- {name} --")

    total_weight = 0 
    for x in source:
        item_obj = source[x]
        name = item_obj.name
        weight = item_obj.weight * item_obj.quantity
        value = item_obj.value
        quantity = item_obj.quantity
        total_weight += weight

        overview = f"{name}: {value}g | {weight} kg | {quantity} copy's."
        print (f"{overview}")
        

    print (f"\nTotal {total_weight}kg's\n")

def container_interaction():
            
    inv_open = True

    player_choice = input("\n----To leave the interaction, type 'Exit'----\nYou want to store or take items?\n 'Take' or 'Store': ").capitalize()
 
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

def trade(Inventory, trader_inventory):

    print("Trader: Welcome mate, what are you buying?\n")
    container_overview(trader_inventory, "Trader")
    item_name = input("Type item name to trade for it: ").capitalize()
    num_item = int(input("How many?: "))


    if item_name in trader_inventory:
        choice_to_buy = input (f"That item costs {trader_inventory[item_name].value} each, you will procceed?: Y or N\n").capitalize()

        if choice_to_buy == "Y":
           if Inventory["Gold"].quantity < trader_inventory[item_name].value * num_item:
               print (f"Trader: Sorry mate, you only have {Inventory["Gold"].quantity} gold, that won't do.")

           if Inventory["Gold"].quantity >= trader_inventory[item_name].value * num_item:
               transfer_items(trader_inventory, Inventory, item_name, num_item)
               Inventory["Gold"].quantity -= trader_inventory[item_name].value * num_item
               print ("Pleasure doing business")
               
               
               

    else:
        print (f"Trader: Sorry Stranger, i have no {item_name} with me")
    
    