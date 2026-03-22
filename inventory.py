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

Chest = {}


def access_inventory(access):
    access = ", " .join(Inventory["Bag"])
    print (access)
    #Place holder for modifying inventory.

def move_inventory_to_chest(Item_name, num_items):

    if Inventory["Bag"][Item_name]["Value"] <= 0:
        print ("You have none of this item")
    else: 
        if Item_name in Chest:
            Chest[Item_name]["Value"] += num_items
            Inventory["Bag"][Item_name]["Value"] -= num_items

        elif Item_name not in Chest:
            Chest[Item_name] = {"Value": Inventory["Bag"][Item_name]}
            Chest[Item_name]["Value"] = num_items
            Inventory["Bag"][Item_name]["Value"] -= num_items


overview = ", " .join(Inventory["Bag"])