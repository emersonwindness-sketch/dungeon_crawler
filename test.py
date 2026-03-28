from inventory import *
from unlock import *
from trade import *
from engine import *
from mechanics.maps.all_maps import *
from mechanics.maps.all_items import *

def container_overview(source):

    if source == Inventory:
        print ("\n----Inventory----\n")

    elif source == Chest:
        print ("\n------Chest------\n")

    for item in source:
        item_obj = source[item]
        
        name = item_obj.name
        weight = item_obj.weight * item_obj.quantity
        value = item_obj.value * item_obj.quantity
        quantity = item_obj.quantity

        overview = f"{name}: {value}g | {weight} kg | {quantity} copy's."
        print (overview)

  
starting_player_items = {

    "Gold": Currency("Gold", 0, 1, 50),
    "Dagger": Items("Dagger", 0.50, 0, 1),
    "Broken lantern": Items("Broken Lanter", 1.50, 0, 1)

}

Inventory = starting_player_items

container_overview(Inventory)




