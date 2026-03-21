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

def move_inventory_to_chest(Inventory, Chest, Item_name, Value):
    for Item_name, Value in Inventory:
        if Item_name in Chest:
            Chest[Item_name][Value] += 1

        elif Item_name not in Chest:
            Chest[Item_name][Value] = 1 



overview = ", " .join(Inventory["Bag"])